# SimpleWebRTC
**URL:** https://assetstore.unity.com/packages/tools/network/simplewebrtc-309727
**Page Title:** SimpleWebRTC | Network | Unity Asset Store
--------------------

LIMITED TIME OFFER: Get a $400+ bundle of top art and tools for JUST $2 !
Over 11,000 five-star assets
Rated by 85,000+ customers
Supported by 100,000+ forum members
Every asset moderated by Unity
SimpleWebRTC is a Unity-based WebRTC wrapper that facilitates  peer-to-peer audio, video, and data communication over WebRTC using Unitys WebRTC package https://docs.unity3d.com/Packages/com.unity.webrtc@3.0/manual/index.html . It leverages WebSockets for signaling and supports both video and audio streaming.
[LINK: https://docs.unity3d.com/Packages/com.unity.webrtc@3.0/manual/index.html](https://docs.unity3d.com/Packages/com.unity.webrtc@3.0/manual/index.html?ampDeviceId=d47430d6-d46e-4e7c-8d6a-815bf191ba80&ampSessionId=1769962416793&ampTimestamp=1770048816797)
A tutorial YouTube video can be found here: https://www.youtube.com/watch?v=-CwJTgt_Z3M
Simple Installation
- Make sure, that the required dependencies are installed (TextMeshPro, Unity WebRTC, NativeWebSocket ( https://github.com/endel/NativeWebSocket )).
[LINK: https://github.com/endel/NativeWebSocket](https://github.com/endel/NativeWebSocket)
- Go to the Unity AssetStore page: https://assetstore.unity.com/packages/slug/309727
- Install the package via Unity AssetStore.
Installation using the releases page
- Got to the releases page and download the latest release from https://github.com/FireDragonGameStudio/SimpleWebRTC/releases
[LINK: https://github.com/FireDragonGameStudio/SimpleWebRTC/releases](https://github.com/FireDragonGameStudio/SimpleWebRTC/releases)
- Make sure, that the required dependencies are installed (TextMeshPro, Unity WebRTC, NativeWebSocket ( https://github.com/endel/NativeWebSocket )).
[LINK: https://github.com/endel/NativeWebSocket](https://github.com/endel/NativeWebSocket)
- Import the package into your Unity project.
Installation using Unity Package Manager
- Create a new Unity project
- Open the Package Manager, click on the + sign in the upper left/right corner
- Select "Add package from git URL"
- Enter URL: https://github.com/endel/NativeWebSocket.git#upm and click in Install
[LINK: https://github.com/endel/NativeWebSocket.git#upm](https://github.com/endel/NativeWebSocket.git#upm)
- After the installation finished, click on the + sign in the upper left/right corner again
- Enter URL https://github.com/FireDragonGameStudio/SimpleWebRTC.git?path=/Assets/SimpleWebRTC#upm and click on Install
[LINK: https://github.com/FireDragonGameStudio/SimpleWebRTC.git?path=/Assets/SimpleWebRTC#upm](https://github.com/FireDragonGameStudio/SimpleWebRTC.git?path=/Assets/SimpleWebRTC#upm)
Installation using Unity Package Manager with preinstalled Meta Voice SDK package
- Create a new Unity project
- The Meta Voice SDK already has the NativeWebSocket package integrated, so there is no need to install it manually. SimpleWebRTC will automatically try to use the NativeWebSocket package provided by Meta.
- Open the Package Manager, click on the + sign in the upper left/right corner
- Select "Add package from git URL"
- Enter URL https://github.com/FireDragonGameStudio/SimpleWebRTC.git?path=/Assets/SimpleWebRTC and click on Install
[LINK: https://github.com/FireDragonGameStudio/SimpleWebRTC.git?path=/Assets/SimpleWebRTC](https://github.com/FireDragonGameStudio/SimpleWebRTC.git?path=/Assets/SimpleWebRTC)
Manual Installation
- Clone the repository: git clone https://github.com/FireDragonGameStudio/SimpleWebRTC
[LINK: https://github.com/FireDragonGameStudio/SimpleWebRTC](https://github.com/FireDragonGameStudio/SimpleWebRTC)
- Open the Unity project in the Unity Editor.
- Ensure that the required dependencies (such as TextMeshPro, Unity WebRTC and NativeWebSocket) are installed.
Usage of WebRTCConnection Component
The WebRTCConnection component manages the WebRTC connection and can be attached to a GameObject in Unity.
Following sample scenes are included in the pacakge:
- WebSocket-TestConnection : For testing the wecksocket connection separately.
- WebRTC-SingleClient-STUNConnection : Testing STUN connection for a single client. Works standalone and can be deployed to clients. Make sure to set the LocalPeerId for each client individually.
- WebRTC-SingleClient-wLobby-STUNConnection : A simple Lobby example for handling multiple STUN WebRTC clients. SimpleLobbyManager.cs shows an example, how to use SimpleWebRTC via C#.
- WebRTC-MultipleClients-STUNConnection : Shows how multiple clients can be connected via peer-to-peer connections and share data, video and audio transmissions.
- WebRTC-SingleClient-STUNConnection-PhotonFusion : Testing STUN connection for a single client. Works standalone and can be deployed to clients. Make sure to set the LocalPeerId for each client individually.
- WebRTC-SingleClient-STUNConnection-VisualScripting : Using Unity Visual Scripting with SimpleWebRTC. Works with all SimpleWebRTC features and can be deployed to clients.
- WebRTC-SingleClient-STUNConnection-ImmersiveSpectator-Sender : A simple example for a possible video sender, which can be every 3D application.
- WebRTC-SingleClient-STUNConnection-ImmersiveSpectator-Receiver : The receiver sample for the video sender. This will most likely targeted at an XR device.
Photon Fusion 2 Integration
- Install Photon Fusion 2 from Unity AssetStore -> Photon Fusion 2
- Import the Photon Fusion sample scene via Unity Package Manager.
- Use the _Generic scripts and PhotonSignalServer to setup the WebRTC connection.
- A tutorial/explanation YouTube video can be found here: https://www.youtube.com/watch?v=z1F_cqfdU6o
WebRTC Web Client
- Make sure your WebSocket signaling server is reachable, up and running.
- Checkout the SimpleWebRTC Web Client
[LINK: SimpleWebRTC Web Client](https://github.com/FireDragonGameStudio/SimpleWebRTC-Web)
- Run npm install in the web client directory, to get everything ready
- Start the web client either locally (npm run dev or npx vite) or deploy it to a webspace
- (Optional) Start your Unity application and make sure the WebRTC logic is up and running.
- Connect all clients to your WebSocket signaling server and wait until the signaling procedure is completed.
- Stream your video, audio and/or data to every connected client.
Support for Unity Visual Scripting
1. Make sure Unity Visual Scripting package is imported.
2. Import SimpleWebRTC Visual Scripting samples.
3. Regenerate Nodes under Edit/Project Settings/Visual Scripting.
4. Mind to add the WebRTCConnectionVisualScriptingEvents component to your WebRTCConnection GameObject.
5. Add your WebRTCConnection GameObject to the scene variables of your graph - look at the sample scene for an example.
Example code
WebRTCConnection connection = gameObject.GetComponent<WebRTCConnection>();
connection.Connect(); // Establish WebSocket connection
// after a WebRTC peer-to-peer connection is established
connection.StartVideoTransmission(); // Begin video streaming
connection.SendDataChannelMessage("Hello Peer!"); // Send a message over the data channel
For further information check https://github.com/FireDragonGameStudio/SimpleWebRTC
[LINK: https://github.com/FireDragonGameStudio/SimpleWebRTC](https://github.com/FireDragonGameStudio/SimpleWebRTC)
- WebRTC peer-to-peer connection management
- WebSocket-based signaling
- Video and audio streaming
- Immersive video streaming (360° monoscopic or stereo over-under)
- Data channel communication
- Logging and debugging tools
- Photon Fusion 2 Integration
- Streaming to web via SimpleWebRTC web client
- Support for Unity Visual Scripting

## Related keywords

## SimpleWebRTC

[LINK: Visit site](https://github.com/FireDragonGameStudio)

## Frequently bought together

## More from FireDragonGameStudio

## Language

## Sell Assets on Unity

## Discover

## Affiliate Program

## Get Asset Store news

## Help

## Feedback

## Partners Program

## Download

## Follow the Asset Store

## Privacy Preference Center

## Privacy Preference Center

- Your Privacy

### Your Privacy

- Functional Cookies

### Functional Cookies

- Performance Cookies

### Performance Cookies

- Targeting Cookies

### Targeting Cookies

- Strictly Necessary Cookies

### Strictly Necessary Cookies

When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. More information
These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.
These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.
These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising. Some 3rd party video providers do not allow video views without targeting cookies. If you are experiencing difficulty viewing a video, you will need to set your cookie preferences for targeting to yes if you wish to view videos from these providers. Unity does not control this.
These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.

### Cookie List

- checkbox label label

--------------------