# Meta Quest Developer Documentation
**URL:** https://developers.meta.com/horizon/documentation/unity/unity-pca-documentation
**Page Title:** Getting Started | Meta Horizon OS Developers
--------------------

[LINK: Other Runtime APIs](/horizon/documentation/unity/unity-haptics-apis/)
[LINK: Overview](/horizon/documentation/unity/unity-depthapi-overview/)
[LINK: Overview](/horizon/documentation/unity/unity-depthapi-occlusions/)
[LINK: Get Started](/horizon/documentation/unity/unity-depthapi-occlusions-get-started/)
[LINK: Advanced Usage](/horizon/documentation/unity/unity-depthapi-occlusions-advanced-usage/)
[LINK: Hands Removal](/horizon/documentation/unity/unity-depthapi-hands-removal/)
[LINK: Samples and Support](/horizon/documentation/unity/unity-depthapi-samples/)
[LINK: API Reference](/horizon/documentation/unity/unity-depthapi-api-reference/)
[LINK: Unity’s XR.Oculus Usage](/horizon/documentation/unity/unity-depthapi-xr-oculus/)
[LINK: Troubleshooting and FAQ](/horizon/documentation/unity/unity-depthapi-troubleshooting-faq/)
[LINK: Developer Posts](/horizon/documentation/unity/ps-developer-posts)
[LINK: Attestation API](/horizon/documentation/unity/ps-attestation-api/)
[LINK: Get Age Category API](/horizon/documentation/unity/ps-get-age-category-api/)
[LINK: In App Update APIs](/horizon/documentation/unity/ps-in-app-update-apis/)
[LINK: OpenXR, VRAPI, and LibOVR](/horizon/documentation/unity/os-openxr-vrapi/)
[LINK: Passthrough API in DroneRage](/horizon/documentation/unity/unity-dronerage-passthrough-api/)
[LINK: Matchmaking API (Deprecated)](/horizon/documentation/unity/ps-matchmaking-api/)

## Getting Started

- Download a sample project and set it up in Unity Editor to explore a passthrough camera using the PassthroughCameraAccess component.
- Display the passthrough texture on a 2D canvas.
- Get the exact pose of an RGB camera in the world-space coordinates and how to orient 2D camera images accurately relative to the physical environment.
- Understand how to access camera data on CPU to write a simple brightness estimation logic.
- Use Unity Sentis to detect real-world objects with ML/CV.
- Write a simple GPU shader to add effects to the passthrough camera.

## Use cases

- Set up and gain access to the Passthrough Camera API using Unity.
- Understand how to integrate with other Meta Quest APIs.
- Understand the organization of the samples and the primary function of each of the samples.
[LINK: Unity-PassthroughCameraApiSamples](https://github.com/oculus-samples/Unity-PassthroughCameraApiSamples)
- CameraViewer sample : shows a 2D canvas with the camera data inside.
- CameraToWorld sample : demonstrates how to align the pose of the RGB camera images with Passthrough, and how 2D image coordinates can be transformed into 3D rays in world space.
- BrightnessEstimation sample : illustrates brightness estimation and how it can be used to adapt the experience to the user’s environment.
- MultiObjectDetection sample : shows how to feed camera data to Unity Sentis to recognize real-world objects. For more information on the Sentis implementation in this sample, please refer to Unity Sentis page.
[LINK: Unity Sentis](https://docs.unity3d.com/Packages/com.unity.sentis@2.1/manual/index.html)
- ShaderSample : demonstrates how to apply custom effects to camera texture on GPU.

## Working with the Passthrough Camera API samples

- Configuring a project
- PassthroughCameraAccess component overview
- Using PassthroughCameraAccess methods to get camera extrinsics, intrinsics, and timestamps
- Overview of the samples to help you get started

### Configuring a Unity project to use PCA

- Clone the GitHub project: https://github.com/oculus-samples/Unity-PassthroughCameraApiSamples
[LINK: https://github.com/oculus-samples/Unity-PassthroughCameraApiSamples](https://github.com/oculus-samples/Unity-PassthroughCameraApiSamples)
- Open the project with Unity 2022.3.58f1 or Unity 6000.0.38f1 . Note : When creating a new Unity project, you must install the MRUK package to access the PassthroughCameraAccess component. See Mixed Reality Utility Kit - Getting Started for installation instructions.
[LINK: Mixed Reality Utility Kit - Getting Started](https://developers.meta.com/horizon/documentation/unity/unity-mr-utility-kit-gs)
- Open ‘Meta / Tools / Project Setup Tool’ and fix any issues that it finds in the configuration of your project.
- Create a new empty scene.
- Select Meta > Tools > Building Blocks from the menu to add the Camera Rig and Passthrough building blocks to your scene. Camera Passthrough API depends on an application running with Passthrough enabled. See Configure your Unity project for instructions on enabling it.
- To integrate Passthrough Camera API, select the ‘Camera Rig’ object in your scene, then enable ‘OVR Manager / Enabled Passthrough Camera Access’ setting and add the PassthroughCameraAccess component to a GameObject in your scene.
- To access the camera texture from a custom C# script, get a reference to the PassthroughCameraAccess component and call its GetTexture() method. The method will return a valid texture only after “horizonos.permission.HEADSET_CAMERA” permission has been granted and the PassthroughCameraAccess is enabled. For example, in the CameraViewer example, the texture is assigned to the RawImage.texture to display it with the Unity UI system.
- Initializing the camera to access the camera data through MRUK.
- Managing camera lifecycle when the component is enabled/disabled or the application is paused.
- Surfacing camera properties including intrinsics, extrinsics, timestamps, and real-time texture data.
- CameraPosition : camera source selection (Left or Right).
- RequestedResolution : desired resolution of the camera images. If the resolution is unsupported, the closest lower resolution is picked instead.
- MaxFramerate : maximum camera stream framerate. Default value is 60 FPS.
- TargetMaterial : automatic update of optional material with the camera texture.
- TexturePropertyName : texture property name to update. Default value is “_MainTex”.
- GetSupportedResolutions(CameraPositionType cameraPosition) - static method that returns an array of all supported resolutions.
- Intrinsics - property that returns the camera intrinsics data: FocalLength, PrincipalPoint, SensorResolution, and LensOffset.

### Mapping camera image to world space

- GetCameraPose() - returns the world pose of the passthrough camera at the current timestamp.
- ViewportPointToRay(Vector2 viewportPoint) - returns a 3D ray in world space which starts from the passthrough camera origin and passes through the viewport point.
- WorldToViewportPoint(Vector3 worldPosition) - transforms a world position to normalized viewport coordinates.
- Timestamp - property that provides the timestamp of the latest camera image.
[LINK: Raycast()](https://developers.meta.com/horizon/reference/mruk/latest/class_meta_x_r_environment_raycast_manager)

### Samples overview

## Best practices

## Troubleshooting

- Check the logs if you encounter errors or crashes. Both the sample and the PassthroughCameraAccess have lots of descriptive log messages that should be able to help you narrow down the problem.
- Make sure ‘ horizonos.permission.HEADSET_CAMERA ’ Android permission is granted to your app. See the Managing Permissions section for instructions on how to manually grant permissions via the command line for debugging.
- When updating the project to Unity version 6 or later, the Android manifest needs to be updated. This can be done either manually or by following these steps: Navigate to Meta > Tools > Update AndroidManifest.xml or Meta > Tools and click Create store-compatible AndroidManifest.xml . Add the ‘ horizonos.permission.HEADSET_CAMERA ’ permission back into the manifest manually after updating. Fix all warnings and errors in the Project Setup Tool after opening the project in the Unity version 6 or later.
- Navigate to Meta > Tools > Update AndroidManifest.xml or Meta > Tools and click Create store-compatible AndroidManifest.xml .
- Add the ‘ horizonos.permission.HEADSET_CAMERA ’ permission back into the manifest manually after updating.
[LINK: Build with Meta](https://developers.meta.com/)
[LINK: Social Technologies](https://developers.facebook.com/)
[LINK: Meta Horizon Creator Program](https://developers.meta.com/horizon-worlds/programs/)
[LINK: Forums](https://communityforums.atmeta.com/category/horizon-developer-forum)
[LINK: Build with Meta](https://developers.meta.com/)
[LINK: Social Technologies](https://developers.facebook.com/)
[LINK: Meta Horizon Creator Program](https://developers.meta.com/horizon-worlds/programs/)
[LINK: Forums](https://communityforums.atmeta.com/category/horizon-developer-forum)
[LINK: Build with Meta](https://developers.meta.com/)
[LINK: Social Technologies](https://developers.facebook.com/)
[LINK: Meta Horizon Creator Program](https://developers.meta.com/horizon-worlds/programs/)
[LINK: Forums](https://communityforums.atmeta.com/category/horizon-developer-forum)

--------------------