import subprocess
import time
from config import CONFIG
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from parameterized_elements import PARAMETERIZED_XPATHS

appium_process = None
emulator_process = None
driver = None

def before_all(context):
    global appium_process, emulator_process, driver
    # Start Appium server once
    command = f'start cmd /k appium --use-plugins=relaxed-caps -p {CONFIG["appium_port"]}'
    appium_process = subprocess.Popen(command, shell=True)
    time.sleep(5)

    # Launch emulator once
    command = f'start cmd /k "{CONFIG["sdk_path"]}\\emulator\\emulator.exe" -avd {CONFIG["emulator_name"]} -no-snapshot-load -gpu host'
    emulator_process = subprocess.Popen(command, shell=True)
    time.sleep(30)
    wait_for_emulator_to_load()

    # Set capabilities once
    desired_caps = {
        'platformName': CONFIG['platform_name'],
        'platformVersion': CONFIG['platform_version'],
        'deviceName': CONFIG['device_name'],
        'automationName': CONFIG['automation_name']
    }
    capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)

    # Start Appium driver once
    driver = webdriver.Remote(command_executor=CONFIG['command_executor'], options=capabilities_options)
    driver.implicitly_wait(20)
    context.driver = driver

    # Open the application once (e.g. Chrome)
    driver.find_element(by=AppiumBy.XPATH,
                        value=PARAMETERIZED_XPATHS['app_by_content_desc'].format(appname=CONFIG["app_name"])).click()

def wait_for_emulator_to_load():
    print("Waiting for the emulator to boot...")
    while True:
        result = subprocess.run(['adb', 'shell', 'getprop', 'sys.boot_completed'], capture_output=True, text=True)
        if result.stdout.strip() == '1':
            print("Boot completed. Checking for home screen...")
            break
        time.sleep(5)

    while True:
        result = subprocess.run(['adb', 'shell', 'pm', 'list', 'packages'], capture_output=True, text=True)
        if CONFIG['launcher_package'] in result.stdout:
            print("Home screen is displayed.")
            break
        time.sleep(5)

def after_all(context):
    global appium_process, emulator_process, driver
    if driver:
        # Close the application
        driver.terminate_app(CONFIG['app_package'])
        driver.quit()
    # Don't terminate processes to avoid killing terminals
    # if emulator_process:
    #     emulator_process.terminate()
    # if appium_process:
    #     appium_process.terminate()

    # Don't kill processes to allow reuse
    # subprocess.run(['taskkill', '/F', '/IM', 'node.exe'])
    # subprocess.run(['taskkill', '/F', '/IM', 'cmd.exe'])
    # subprocess.run(['taskkill', '/F', '/IM', 'qemu-system-x86_64.exe'])
