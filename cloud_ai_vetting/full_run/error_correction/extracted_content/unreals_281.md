# Unreal's
**URL:** https://dev.epicgames.com/community/learning/tutorials/aqV9/render-hardware-interface-rhi
**Page Title:** Render Hardware Interface (RHI) | Epic Developer Community
--------------------

[LINK: Create tutorial now](https://dev.epicgames.com/community/api/user_identity/login/start?destination=https%3A%2F%2Fdev.epicgames.com%2Flearning%2Ftutorials%2Fnew)
The Render Hardware Interface (RHI) is an abstraction layer over several platform-specific graphics APIs. It is designed from the ground up to take advantage of DirectX 12, Vulkan, and Metal 2.0.
[LINK: Render Hardware Interface (RHI)](https://www.o3de.org/docs/atom-guide/dev-guide/rhi/rhi/)
In order to change the RHI settings in your UE5 project, you can either:
Edit  "...../path_to_your_UE5_project/config/DefaultEngine.ini" and change DefaultGraphicsRHI=DefaultGraphicsRHI_DX12 to your preferred RHI (e.g. DX11 or Vulkan)
See an example below to use DirectX 11 instead of 12:
[/Script/WindowsTargetPlatform.WindowsTargetSettings]
DefaultGraphicsRHI=DefaultGraphicsRHI_DX11
Go to “Edit → Project settings → Platforms → Windows → Default RHI” and select DirectX 11 or Vulkan.
Please note that, in the current version of UE5 released on 5-April-2022 and earlier versions, there is an exhausted video memory message which appears when using the default RHI (DX12) on Windows with lumen (as a Dynamic Global Illumination Method). Using other methods would remove the message however the UE5 Engine will eventually crash with  the "GPU crashed or D3D Device Removed" Error.  To get rid of both errors, I used DirectX 11 as my RHI device. I didn't test Vulkan yet.
See  the figure below.
Enjoy!
Shabayek
- Rendering
- Film & TV
- Architecture
- Visualization
- Games
- performance & profiling

--------------------