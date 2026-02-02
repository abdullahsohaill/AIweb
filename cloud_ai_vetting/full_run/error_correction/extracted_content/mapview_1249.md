# MapView
**URL:** https://docs.expo.dev/versions/latest/sdk/map-view
**Page Title:** react-native-maps - Expo Documentation
--------------------

Reference version

## react-native-maps

A library that provides a Map component that uses Google Maps on Android and Apple Maps or Google Maps on iOS.
[LINK: GitHub](https://github.com/react-native-maps/react-native-maps)
GitHub
npm
react-native-maps provides a Map component that uses Google Maps on Android and Apple Maps or Google Maps on iOS.
No additional setup is required when testing your project using Expo Go. However, to deploy the app binary on app stores additional steps are required for Google Maps. For more information, see the instructions below .

## Installation

If you are installing this in an existing React Native app , make sure to install expo in your project. Then, follow the installation instructions provided in the library's README or documentation.
[LINK: installation instructions](https://github.com/react-native-maps/react-native-maps/blob/master/docs/installation.md)

## Usage

See full documentation at react-native-maps/react-native-maps .
[LINK: react-native-maps/react-native-maps](https://github.com/react-native-maps/react-native-maps)

## Deploy app with Google Maps

### Android

If you have already registered a project for another Google service on Android, such as Google Sign In, you enable the Maps SDK for Android on your project and jump to step 4.
- Open your browser to the Google API Manager and create a project.
[LINK: Google API Manager](https://console.developers.google.com/apis)
- Once it's created, go to the project and enable the Maps SDK for Android .
- If you are deploying your app to the Google Play Store , you'll need to upload your app binary to Google Play console at least once. This is required for Google to generate your app signing credentials.
- Go to the Google Play Console > (your app) > Release > Setup > App integrity > App Signing .
- Copy the value of SHA-1 certificate fingerprint .
- If you have already created a development build , your project will be signed using a debug keystore.
- After the build is complete, go to your project's dashboard , then, under Configure > click Credentials .
- Under Application Identifiers , click your project's package name and under Android Keystore copy the value of SHA-1 Certificate Fingerprint .
- Go to Google Cloud Credential manager and click Create Credentials , then API Key .
[LINK: Google Cloud Credential manager](https://console.cloud.google.com/apis/credentials)
- In the modal, click Edit API key .
- Under Key restrictions > Application restrictions , choose Android apps .
- Under Restrict usage to your Android apps , click Add an item .
- Add your android.package from app.json (for example: com.company.myapp ) to the package name field.
- Then, add the SHA-1 certificate fingerprint's value from step 2.
- Click Done and then click Save .
- Copy your API Key into your your to either a .env file and then add it to your app.json under the android.config.googleMaps.apiKey field like or copy it:
- In your code, import { PROVIDER_GOOGLE } from react-native-maps and add the property provider={PROVIDER_GOOGLE} to your <MapView> . This property works on both Android and iOS.
- Rebuild the app binary (or re-submit to the Google Play Store in case your app is already uploaded). An easy way to test if the configuration was successful is to do an emulator build .

### iOS

If you have already registered a project for another Google service on iOS, such as Google Sign In, you enable the Maps SDK for iOS on your project and jump to step 3.
- Open your browser to the Google API Manager and create a project.
[LINK: Google API Manager](https://console.developers.google.com/apis)
- Then, go to the project, click Enable APIs and Services and enable the Maps SDK for iOS .
- Go to Google Cloud Credential manager and click Create Credentials , then API Key .
[LINK: Google Cloud Credential manager](https://console.cloud.google.com/apis/credentials)
- In the modal, click Edit API key .
- Under Key restrictions > Application restrictions , choose iOS apps .
- Under Accept requests from an iOS application with one of these bundle identifiers , click the Add an item button.
- Add your ios.bundleIdentifier from app.json (for example: com.company.myapp ) to the bundle ID field.
- Click Done and then click Save .
- Copy your API Key into your your to either a .env file and then add it to your app.json under the ios.config.googleMapsApiKey field like or copy it:
- In your code, import { PROVIDER_GOOGLE } from react-native-maps and add the property provider={PROVIDER_GOOGLE} to your <MapView> . This property works on both Android and iOS.
- Rebuild the app binary. An easy way to test if the configuration was successful is to do a simulator build .

--------------------