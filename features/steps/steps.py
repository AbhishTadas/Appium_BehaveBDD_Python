from appium.webdriver.common.appiumby import AppiumBy

from behave import given, when, then

from config import CONFIG
from elements import NORMAL_XPATHS
from parameterized_elements import PARAMETERIZED_XPATHS

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@then('I click on the "{element}"')
def step_then_i_click_on_the(context, element):
    """
    Clicks on the specified element using its content description.

    This step locates an image button by its content description and performs a click action.
    The element is identified using a parameterized XPath from PARAMETERIZED_XPATHS.

    Args:
        context: The Behave context object containing the driver.
        element: The content description of the element to click (e.g., "Options for Discover").
    """
    context.driver.find_element(by=AppiumBy.XPATH,
                                value=PARAMETERIZED_XPATHS['image_button_by_content_desc'].format(element=element)).click()

@then('"{option}" the discovered feed')
def step_then_the_discovered_feed(context, option):
    """
    Toggles the discovered feed option in the Chrome menu.

    This step attempts to find and click the specified option ("Turn on" or "Turn off").
    If the option is not found, it clicks the opposite option, then opens the "Options for Discover" menu,
    and finally clicks the desired option. The menu closes automatically after the click.

    Args:
        context: The Behave context object containing the driver.
        option: The option to select ("Turn on" or "Turn off").
    """
    try:
        option_element = context.driver.find_element(by=AppiumBy.XPATH,
                                                     value=PARAMETERIZED_XPATHS['discovered_feed_option'].format(option=option))
        option_element.click()
    except:
        opposite = "Turn on" if option == "Turn off" else "Turn off"
        opposite_element = context.driver.find_element(by=AppiumBy.XPATH,
                                                       value=PARAMETERIZED_XPATHS['discovered_feed_option'].format(option=opposite))
        opposite_element.click()
        step_then_i_click_on_the(context, "Options for Discover")
        option_element = context.driver.find_element(by=AppiumBy.XPATH,
                                                     value=PARAMETERIZED_XPATHS['discovered_feed_option'].format(option=option))
        option_element.click()


@then('the discovered feed should be "{expected_state}"')
def step_then_verify_discovered_feed_state(context, expected_state):
    """
    Verifies that the discovered feed is in the expected state.

    This step waits up to 2 seconds for an element with the expected state text to be present.
    If the element is not found within the timeout, the test fails with an assertion error.

    Args:
        context: The Behave context object containing the driver.
        expected_state: The expected state of the discovered feed ("Turn on" or "Turn off").
    """
    try:
        WebDriverWait(context.driver, 2).until(
            EC.presence_of_element_located((AppiumBy.XPATH, PARAMETERIZED_XPATHS['discovered_feed_option'].format(option=expected_state)))
        )
    except:
        assert False, f"Expected discovered feed state to be '{expected_state}', but not found within 2 seconds"

