# Appium Python with Behave BDD Framework

A basic code example for automating mobile applications using Appium with Python and the Behave BDD framework.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Project Structure and Functionality](#project-structure)
- [What the Automation Does](#what-the-automation-does)
- [How to Execute](#how-to-execute)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Future Scope/TODO](#future-scope-todo)

## Requirements

1. **NodeJS** - Required to install Appium
2. **Python** - Programming language for automation scripts
3. **Java** - Required for running SDKManager commands
4. **Appium** - Mobile automation framework
5. **Appium Inspector** - Tool for inspecting mobile app elements
6. **Android packages** (Can be installed via Android Studio)
7. **Editor** - PyCharm or Visual Studio Code

## Installation

### Install Appium
```bash
npm install -g appium
```

### Install Android Packages
1. Download Commandline tools and platform tools from the Android Studio website
2. Create a new folder named 'latest' in the commandline tools folder
3. Move all files from the commandline tools folder to the 'latest' folder
4. Set `ANDROID_HOME` and `ANDROID_SDK_ROOT` environment variables to point to the Commandline tools folder location
5. Navigate to the sdkmanager location in the commandline folder and run:
   ```bash
   sdkmanager "platform-tools" "platforms;android-XX" "emulator" "build-tools;<version_number>"
   ```
6. Update SDKManager if needed:
   ```bash
   sdkmanager --update
   ```
7. Create an AVD (Android Virtual Device):
   ```bash
   avdmanager create avd -n <avdname> -k "system-images;android-XX;google_apis;x86_64"
   ```
   (Replace XX with the Android version number)

8. List available emulators:
   ```bash
   emulator -list-avds
   ```

9. Start an emulator:
   ```bash
   emulator -avd <avdname>
   ```

10. For better performance:
    ```bash
    emulator -avd <avdname> -no-boot-anim -gpu host
    ```

11. Folder structure for Android folder 
 ```
   Android/
   ├── build-tools
   ├── cmake
   ├── cmdline-tools
       ├── latest
           ├── bin (Should contain avdmanager.bat and sdkmanager.bat)
           ├── lib
   ├── emulator (should contain emulator.exe)
   ├── licenses
   ├── ndk 
   ├── platform-tools (should contain adb.exe)
   ├── platforms
   ├── sources
   └── system-images
   ```

### Get AppActivity and AppPackage
To find the AppActivity and AppPackage of an app:
1. Connect your device and ensure the app is active
2. Run:
   ```bash
   adb shell
   dumpsys window displays | grep -E "mCurrentFocus"
   ```
3. This command returns the AppPackage/AppActivity format
   Example: `com.android.chrome/com.google.android.apps.chrome.Main`

### Install Python Packages
```bash
pip install Appium-Python-Client
pip install behave
```

## Project Structure and Functionality

The project is organized under the `features/` directory with the following files and their functionality:

- **`features/config.py`**:
  - Stores all configuration values to eliminate hardcoding.
  - Includes paths (e.g., SDK path)
  - Includes ports (e.g., Appium port)
  - Includes device details (e.g., platform, version, name)
  - Includes app information (e.g., package, name)
  - Includes UI element identifiers
  - Centralizes constants for easy maintenance and updates.

- **`features/environment.py`**:
  - Contains Behave hooks for test lifecycle management.
  - `before_all()`:
    - Starts Appium server once for all tests.
    - Launches Android emulator once.
    - Sets up Appium driver capabilities.
    - Opens the Chrome app once.
  - `after_all()`:
    - Closes the app and driver.
    - Does not kill terminal processes to allow reuse.
  - Ensures efficient setup and teardown across all scenarios.

- **`features/steps/steps.py`**:
  - Implements step definitions for BDD scenarios.
  - Handles user interactions such as clicking elements and toggling features.
  - Contains logic for conditional actions (e.g., toggling discovered feed with fallback).
  - Uses explicit waits for reliable verifications and assertions.
  - Each step function is well-documented with docstrings explaining purpose, behavior, and parameters.

- **`features/Test.feature`**:
  - Defines BDD scenarios using Gherkin syntax.
  - Includes scenarios for turning the discovered feed on and off.
  - Uses Given-When-Then format for clarity.
  - Supports multiple test cases with shared setup.

- **`features/elements.py`**:
  - Contains normal (static) XPath expressions.
  - Defines fixed locators for UI elements that remain constant.
  - Examples include menu items and buttons with consistent identifiers.
  - Improves code readability and maintainability.

- **`features/parameterized_elements.py`**:
  - Stores parameterized XPath expressions with placeholders.
  - Allows dynamic element location based on runtime values.
  - Supports flexible locators for elements with variable content (e.g., app names, option texts).
  - Enhances reusability across different test scenarios.

## What the Automation Does

This automation framework tests the "Discovered Feed" feature in the Google Chrome mobile app using Appium and Behave BDD. Here's a detailed breakdown:

### Key Features and Optimizations

1. **Efficient Setup and Teardown**:
   - The `before_all` hook starts the Appium server and Android emulator only once at the beginning of the test suite.
   - The Chrome app is launched once and remains open throughout all test scenarios.
   - This approach saves significant execution time by avoiding repeated setup for each test, leveraging the state from previous tests.

2. **State Management**:
   - The application state (e.g., whether the discovered feed is on or off) persists between scenarios.
   - Test 1 may leave the feed in a certain state, and Test 2 uses that state as the starting point, reducing redundant actions and improving performance.

3. **Element Location Strategies**:
   - **Normal XPaths**: Defined in `features/elements.py`, these are fixed XPath expressions for elements with consistent locators, such as `//android.widget.TextView[@resource-id="com.android.chrome:id/menu_item_text"]` for the discovered feed menu item.
   - **Parameterized XPaths**: Defined in `features/parameterized_elements.py`, these use placeholders for dynamic content, like `//android.widget.TextView[@content-desc="{appname}"]` for app icons or `//android.widget.TextView[@resource-id="com.android.chrome:id/menu_item_text" and @text="{option}"]` for menu options with specific text.

4. **Test Scenarios**:
   - **Scenario 1**: Turns off the discovered feed and verifies the state changes to "Turn on".
   - **Scenario 2**: Turns on the discovered feed and verifies the state changes to "Turn off".
   - Each scenario opens the options menu, performs the toggle action, and asserts the expected state using WebDriverWait for reliable element detection.

5. **Error Handling and Verification**:
   - The toggle logic includes try-except blocks to handle cases where the expected option is not immediately available.
   - Verification steps use explicit waits (up to 2 seconds) to locate elements with expected text, providing clear failure messages if the state doesn't match.

6. **Resource Management**:
   - Processes are not forcibly killed to prevent terminal closure, allowing for faster subsequent test runs.
   - The framework ensures clean shutdown of the app and driver in the `after_all` hook.

This setup demonstrates best practices for mobile automation, including efficient resource usage, maintainable element locators, and robust state handling across test scenarios.

## How to Execute

Run the following command to execute the tests:
```bash
behave
```

## Configuration

### Modifying `features/config.py`

The `config.py` file contains all configurable values for the automation framework. To customize for your environment:

1. **SDK Path**: Update `'sdk_path'` to the path where Android SDK is installed (e.g., `'C:\\Android\\Sdk'` on Windows).
2. **Appium Port**: Change `'appium_port'` if the default port 4723 is in use.
3. **Device Details**: Modify `'platform_version'`, `'device_name'`, etc., to match your target device or emulator.
4. **Emulator Name**: Update `'emulator_name'` to the name of your AVD.
5. **App Name**: Change `'app_name'` to the app you want to test (ensure the content-desc matches).
6. **UI Elements**: Adjust XPath-related constants if the app UI changes.

### Environment Variables

Ensure the following environment variables are set:
- `ANDROID_HOME`: Path to Android SDK root.
- `ANDROID_SDK_ROOT`: Same as `ANDROID_HOME`.
- `JAVA_HOME`: Path to JDK installation.
- `PATH`: Include paths to `adb`, `emulator`, `node`, and `npm`.

### Command Line Options

You can pass tags to Behave for selective test execution:
```bash
behave --tags @smoke
```

## Troubleshooting

### Common Issues and Solutions

1. **Appium Server Fails to Start**
   - **Issue**: Port already in use or permissions error.
   - **Solution**: Change the port in `config.py` or kill the process using the port: `netstat -ano | findstr :4723` then `taskkill /PID <PID>`.

2. **Emulator Not Launching**
   - **Issue**: AVD not found or hardware acceleration disabled.
   - **Solution**: Verify AVD name in `config.py` matches `emulator -list-avds`. Enable VT-x/AMD-V in BIOS for hardware acceleration.

3. **ADB Not Found**
   - **Issue**: `adb` command not recognized.
   - **Solution**: Add `platform-tools` to PATH or update `'sdk_path'` in `config.py`.

4. **Element Not Found Errors**
   - **Issue**: XPath locators outdated due to app updates.
   - **Solution**: Use Appium Inspector to inspect elements and update XPaths in `elements.py` or `parameterized_elements.py`.

5. **Driver Initialization Fails**
   - **Issue**: Capabilities mismatch or device not ready.
   - **Solution**: Ensure emulator is fully booted (check with `adb devices`). Verify capabilities in `config.py`.

6. **Tests Hanging or Timing Out**
   - **Issue**: Implicit waits too short or emulator slow.
   - **Solution**: Increase `implicitly_wait` in `environment.py` or add explicit waits using `WebDriverWait`.

7. **Python Import Errors**
   - **Issue**: Missing packages.
   - **Solution**: Run `pip install -r requirements.txt` (create if needed) or install individually: `pip install Appium-Python-Client behave selenium`.

8. **Permission Denied on Windows**
   - **Issue**: UAC blocking execution.
   - **Solution**: Run command prompt as administrator or adjust UAC settings.

### Debugging Tips

- Enable verbose logging: `behave -v`
- Check Appium logs in the terminal where server is running.
- Use `adb logcat` to view device logs.
- Verify Python version compatibility (3.7+ recommended).

## Future Scope/TODO

### Planned Enhancements

1. **Expand Test Coverage**
   - Add scenarios for other Chrome features (e.g., bookmarks, history, settings).
   - Include negative test cases (e.g., invalid inputs, error handling).
   - Test on multiple devices and screen sizes.

2. **iOS Support**
   - Adapt the framework for iOS testing using XCUITest.
   - Update capabilities and locators for iOS-specific elements.

3. **CI/CD Integration**
   - Integrate with Jenkins, GitHub Actions, or Azure DevOps.
   - Automate test execution on pull requests and merges.
   - Generate reports and notifications.

4. **Reporting and Analytics**
   - Implement Allure or ExtentReports for detailed test reports.
   - Add screenshots on failure.
   - Track test execution metrics and trends.

5. **Performance Testing**
   - Measure app launch times, UI response times.
   - Integrate with tools like Lighthouse for web app performance.

6. **Parallel Execution**
   - Run tests in parallel on multiple devices/emulators.
   - Use Selenium Grid or Appium Grid for distributed execution.

7. **Data-Driven Testing**
   - Support CSV/Excel for test data.
   - Parameterize tests with different user profiles or configurations.

8. **Security Testing**
   - Integrate with tools like OWASP ZAP for web security scans.
   - Test app permissions and data handling.

9. **Accessibility Testing**
   - Add checks for screen reader compatibility.
   - Validate color contrast and touch target sizes.

10. **Maintenance and Best Practices**
    - Implement Page Object Model for better code organization.
    - Add linting and code quality checks.
    - Create documentation for custom locators and utilities.
