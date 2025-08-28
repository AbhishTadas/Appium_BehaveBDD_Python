# Appium_Python_with_BehaveBDD

## This a very basic code to automate mobile application with the help of appium in python language with wit BDD framework.

## Table of Content
- [Requirement](#requirement)
- [Installation](#installation)

## Requirement
1. NodeJS - required to install appium
2. Python
3. java - required for running SDKManager command
4. Appium
5. Appium Inspector
6. Android packages (You can use Android Studio)
7. Editor - Pycharm/Visual Studio Code

## Installation
Install appium 
- npm install -g appium  

Install Android Package  
- Download Commandline tools and platform tools form Android studio website.
- Create a new folder in the commandline tools folder and name it 'latest'. Then move all the folder present in the commandline tools folder to the 'latest' folder.
- Set ANDROID_HOME and ANDROID_SDK_ROOT to location of the Commandline tools folder.
- navigate to the sdkmanager location in te commandline folder and run the command =>sdkmanager "platform-tools" "platforms;android-XX" "emulator" "build-tools;<version_number>" 
- old SDKmanager sometime not work so update it with the command - sdkmanager --update
- Create AVD with the command - avdmanager create avd -n <avdname> -k "system-images;android-XX;google_apis;x86_64" XX is the version number.
- To list the emulators - emulator -list-avds
- To start the emulator - emulator -avd <avdname>
- To improve performance - emulator -avd <avdname> -no-boot-anim -gpu host
- To know the AppActivity and AppPackage
   adb shell (device must be connected and app must be active)
   dumpsys window displays | grep -E “mCurrentFocus”
  This command gives the AppActivity and AppPackage of the current focus app. The format is AppPackage/AppActivity.
  Example - com.android.chrome/com.google.android.apps.chrome.Main

python packages
pip install Appium-Python-Client
pip install behave
  
How to execute:
    run command "behave"