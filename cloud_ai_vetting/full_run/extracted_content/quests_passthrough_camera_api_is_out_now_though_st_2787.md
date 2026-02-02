# Quest's Passthrough Camera API Is Out Now, Though Store Apps Can't Yet Use It
**URL:** https://www.uploadvr.com/quest-passthrough-camera-api-experimental-out-now
**Page Title:** Quest Passthrough Camera API Out Now For Developers To Play With
--------------------


## Quest 3's Passthrough Camera API Is Out Now, Though Store Apps Can't Yet Use It

- Share to Reddit
[LINK: Share to Reddit](https://www.reddit.com/submit?url=https://www.uploadvr.com/quest-passthrough-camera-api-experimental-out-now/&title=Quest%203's%20Passthrough%20Camera%20API%20Is%20Out%20Now%2C%20Though%20Store%20Apps%20Can't%20Yet%20Use%20It)
- Share to Facebook
[LINK: Share to Facebook](https://www.facebook.com/sharer/sharer.php?u=https://www.uploadvr.com/quest-passthrough-camera-api-experimental-out-now/)
- Share to WhatsApp
[LINK: Share to WhatsApp](whatsapp://send?text=https://www.uploadvr.com/quest-passthrough-camera-api-experimental-out-now/)
Quest 3's highly anticipated "Passthrough Camera API" is now available for all developers to experiment with, though they can't yet include it in store app builds.
The new capability was announced at Meta Connect 2024 in September as coming this year. Now it's here, as an experimental release for Quest 3 and Quest 3S. That means any developer can experiment with it, and even distribute APKs using it on platforms like SideQuest, but they can't yet include it in Meta Horizon Store apps. Meta has taken this approach for new APIs multiple times in the past, and typically makes the feature available for use in store apps within a few months at most.
[LINK: announced at Meta Connect 2024](https://www.uploadvr.com/quest-passthrough-api-camera-access-next-year/)
Select developers have had early access to experiment with the capability for a while now, and Meta will host Niantic, Creature, and Resolution to discuss it at GDC next week .
[LINK: have had early access](https://www.uploadvr.com/niantic-creature-resolution-games-already-using-quest-passthrough-api/)
[LINK: at GDC next week](https://www.uploadvr.com/niantic-creature-resolution-games-already-using-quest-passthrough-api/)
While headsets like Quest 3 use cameras to let you see the real world, until now only the system software got raw access to these cameras. Third-party developers could use passthrough as a background, sure, but they didn't actually get access to it. They instead got higher-level data derived by the system, such as hand and body skeletal coordinates, a 3D mesh of your environment with bounding boxes for furniture, and limited object tracking capabilities. That meant they couldn't run their own computer vision models, which severely limited the augmentation capabilities of these headsets. The exception was that on visionOS 2, Apple gives enterprise companies raw access to Vision Pro's passthrough cameras for non-public internal apps, but this requires a special licence from Apple and is restricted to "in a business setting only".
For the "Passthrough Camera API" to work, you as the user need to grant the app permission to access your headset cameras, just as you would the microphone. If granted, the app gets access to the forward-facing color cameras, including metadata like the lens intrinsics and headset pose, which it can leverage to run custom computer vision models.
Examples of how apps could use this include scanning and tracking QR codes, detecting a game board on a table to add virtual characters and objects to it, detecting physical objects for enterprise guide experiences, or integrating the visual AI functionality of cloud-hosted large language models (LLMs). Developers are only limited by which real-time computer vision models can run on the XR2 Gen 2 chipset performantly, or which cloud-hosted image models they're willing to pay for.
Meta software engineer Roberto Coviello's QuestCameraKit samples.
The passthrough camera stream is provided to the app with up to 1280 × 960 resolution per camera at 30FPS, with a stated latency of 40-60 milliseconds. That means it isn't suitable for tracking fast moving objects, such as custom controllers, nor for discerning fine features like small text.
Technically, at a base level, there is no specific Meta Quest Camera Passthrough API, nor is it an extension to OpenXR. Developers do need to request a Horizon OS specific Headset Cameras permission, but otherwise Quest's passthrough camera access leverages Android's existing Camera2 API to also return the headset pose, obtained with OpenXR, and the Camera2 API is what developers of custom engines, or source code for Unreal or Godot, use for it. This also means the same code should work on Google's upcoming Android XR platform , set to debut in Samsung's standalone headset, with only the permission request being different.
[LINK: Google's upcoming Android XR platform](https://www.uploadvr.com/android-xr-will-give-developers-passthrough-access/)
For Unity, developers can easily access the cameras through Unity's WebCamTexture API, which is how they already access phone, tablet, and PC cameras and webcams in the engine. A limitation here, however, is that Unity's WebCamTexture API only supports one camera at a time, not both.
Walkthrough from Meta software engineer Roberto Coviello.
Interested developers can find Quest passthrough camera access documentation here: Unity / Native Android .
[LINK: Unity](https://developers.meta.com/horizon/documentation/unity/unity-pca-documentation?ref=uploadvr.com)
[LINK: Native Android](https://developers.meta.com/horizon/documentation/native/android/pca-native-documentation?ref=uploadvr.com)
Meta has published five official Unity samples on GitHub: CameraViewer, CameraToWorld, BrightnessEstimation, MultiObjectDectection, ShaderSample. Meta software engineer Roberto Coviello has separately published QuestCameraKit on GitHub, a collection of five further samples: Color Picker, Object Detection with Unity Sentis, QR Code Tracking with ZXing, Frosted Glass Shader, and OpenAI vision model.
[LINK: official Unity samples](https://github.com/oculus-samples/Unity-PassthroughCameraApiSamples?ref=uploadvr.com)
[LINK: QuestCameraKit](https://github.com/xrdevrob/QuestCameraKit?ref=uploadvr.com)

### Meta Interaction SDK Gets Hand Tracking Climbing, Improved Locomotion & Throwing

### Weekly Newsletter

Get a weekly summary of the most important VR and AR news.

### Meta's Smart Glasses SDK Is Now Available To Build With, But Not Yet To Ship

### Meta's WorldGen AI-Generates 3D Worlds From A Text Prompt

Unlock the full potential of UploadVR and support our independent journalism with an ad-free experience by becoming a Member.

## Community Discussion

## Weekly Newsletter

Sign up to get a weekly summary of the most important VR and AR news, straight to your inbox.

## More App Development

### Meta Interaction SDK Gets Hand Tracking Climbing, Improved Locomotion & Throwing

### Meta's Smart Glasses SDK Is Now Available To Build With, But Not Yet To Ship

### Meta's WorldGen AI-Generates 3D Worlds From A Text Prompt

### Godot Now Supports More XR Features & Builds A Universal OpenXR APK

## Latest Articles

### Attending Lakers Games In Apple Immersive Plays To VR's Strengths

### Walkabout Mini Golf Studio Mighty Coconut Course Corrects With Layoffs, $1 More For Future DLC

### Meta CTO Explains Layoffs & Strategy Shift: "VR Is Growing Less Quickly Than We Hoped"

### Lovecraftian Horror Dread Meridian Struggles With Combat

### Golden Gloves VR Debuts As Scrappy Contender On Quest Headsets

### Salmon Man Review: Paddling Up The River Against Extreme Frustration

### Cyberpunk 2077 VR Mod Needs To Be Free, Dev Says After Removal

### Real VR Fishing Sold One Million Copies So Far

### Thief VR: Legacy of Shadow Rolls Out Graphical Improvements

### Guardians Frontline's New Update Adds User-Made Campaigns

### Memoreum Director Tries Patreon & Sideloading To Distribute New Quest Game

### Palmer Luckey: Meta Isn't Abandoning VR, Studio Closures "A Good Thing"

### Attending Lakers Games In Apple Immersive Plays To VR's Strengths

### Walkabout Mini Golf Studio Mighty Coconut Course Corrects With Layoffs, $1 More For Future DLC

### Meta CTO Explains Layoffs & Strategy Shift: "VR Is Growing Less Quickly Than We Hoped"

### Lovecraftian Horror Dread Meridian Struggles With Combat

### Golden Gloves VR Debuts As Scrappy Contender On Quest Headsets

### Salmon Man Review: Paddling Up The River Against Extreme Frustration

### Cyberpunk 2077 VR Mod Needs To Be Free, Dev Says After Removal

### Real VR Fishing Sold One Million Copies So Far

### Thief VR: Legacy of Shadow Rolls Out Graphical Improvements

### Guardians Frontline's New Update Adds User-Made Campaigns

### Memoreum Director Tries Patreon & Sideloading To Distribute New Quest Game

### Palmer Luckey: Meta Isn't Abandoning VR, Studio Closures "A Good Thing"


--------------------