
<img src="https://raw.githubusercontent.com/Spyxpo/spyxpo-web-to-app-builder/dev/images/logo.png" width="50" height="50">

# Spyxpo Web to App Builder

**Convert any website into an iOS/Android/Windows/macOS/Linux app.**

This is a preview build for testing purposes major update coming soon.

## Supported OS

- Windows
- macOS
- Linux

## Steps

- [Requirements](#requirements)
- [Installation](#installation)
- [Update](#update)
- [Release](#release)
- [Known Issues](#known-issues)

## Screenshots

![App Screenshot](https://raw.githubusercontent.com/Spyxpo/spyxpo-web-to-app-builder/dev/screenshots/screenshot-1.png)



<a id= "requirements"></a>

## Requirements

Add flutter SDK, Android Studio, Xcode, Python3 and JRE in PATH(if required).

- [Flutter >=2.12.0 <3.0.0](https://flutter.dev/docs/get-started/install)
- [Python 3.8 or above](https://www.python.org)
- [Android Studio](https://developer.android.com/studio?gclid=CjwKCAiA1aiMBhAUEiwACw25MR3VaqSxOs-Xh0t0pI8ZyjjpdArTBE45Yqvdo5BAMC4ETrX0AHcqoBoCodAQAvD_BwE&gclsrc=aw.ds)
- [Xcode (only for macOS)](https://apps.apple.com/us/app/xcode/id497799835?mt=12)
- [Java JRE (for Keystore)](https://www.java.com/en/download/)
- [Git](https://git-scm.com/downloads)

<a id= "installation"></a>
## Installation

```bash
git clone https://github.com/Spyxpo/spyxpo-web-to-app-builder.git
cd spyxpo-web-to-app-builder
python3 run.py
```

or

```bash
git clone https://github.com/Spyxpo/spyxpo-web-to-app-builder.git
cd spyxpo-web-to-app-builder
python run.py
```

<a id= "update"></a>
## Update

```bash
cd spyxpo-web-to-app-builder
git pull
```
or
```bash
cd spyxpo-web-to-app-builder
python3 update.py
```
or
```bash
cd spyxpo-web-to-app-builder
python update.py
```
<a id= "release">

<a id= "known-issues"></a>
## Known Issues

All issues that are known to us are listed here, we are working on fixing them.
- "key.properties" file is not generated properly so app is not signed completely.
- Migrate plugin 'flutter_webview_plugin' to [V2 embedding ](https://flutter.dev/go/android-plugin-migration).


## Release

#### Create a Keystore (For signing app and uploading on Play Store)
Keep your keystore file backed up(backup .jks file, alias name and passwords of your keystore file)

```bash
keytool -genkey -v -keystore ~/upload-keystore.jks -keyalg RSA -keysize 2048 -validity 10000 -alias upload -storetype JKS
```

## Features

- Website to apk
- Website to aab
- App works without internet
- Javascript enabled
- Play Store ready app
- Custom keystore for aab signing

## Coming soon

- Convert website into ipa/app/exe/appimage
- External url opener
- Pull to refresh
- Notifications
- App update popup
- Dockerizing this project soon

## Authors

- [Mantresh Khurana](https://github.com/mantreshkhurana/)
