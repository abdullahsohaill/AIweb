# VDO.Ninja
**URL:** https://vdo.ninja
**Page Title:** VDO.Ninja
--------------------

[LINK: Terms of Service](https://docs.vdo.ninja/help/privacy-and-security-details/vdo.ninja-terms-of-service)
[LINK: Privacy Policy](https://docs.vdo.ninja/help/privacy-and-security-details/vdo.ninja-privacy-policy)
[LINK: Report Abuse](https://docs.vdo.ninja/help/privacy-and-security-details/abuse-and-child-safety)

## Create a Room

- Disabling video sharing between guests will improve performance
- Invite only guests to the room that you trust.
- The "Recording" option is considered experimental.
- Advanced URL parameters are available to customize rooms.

## Add your Camera to OBS

Privacy warning: The director will be able to remotely change your camera, microphone, and URL.
For the best possible experience, make sure
- No Audio
Consider using a Chromium-based browser instead. Safari is more prone to having audio issues
We've detected that you are using an old version of Apple iOS. Please consider updating if facing issues.

## Add your Microphone to OBS

## Remote Screenshare into OBS

Privacy warning: The director will be able to remotely change your camera, microphone, and URL while this page is open, if you continue.

### Things to Note

- Screen audio selection will be handled by your browser's sharing dialog
- Additional microphone sources can be added and will be mixed with your screen audio
- Quality settings affect maximum capture resolution - lower settings may be smoother
- For application-specific audio capture, see here
[LINK: see here](https://docs.vdo.ninja/audio)
- For achieving 1080p60 game-capture, see here
[LINK: see here](https://docs.vdo.ninja/guides/how-to-screen-share-in-1080p)

## Create Reusable Invite

[LINK: documentation](https://docs.vdo.ninja/advanced-settings)

## Stream Media File

## Warning

Media file streaming is still quite experimental. Please do not rely on it heavily for your productions. Feedback welcome.

## Chrome/Edge users

Keep this tab visible, else the video playback will stop

## Safari Users

Safari does not support this feature. Consider Chrome or Firefox instead.

## Share Website

## Usage information

- Not all websites will work with this feature as some sites disallow embedding.
- The site will try to auto-optimize standard Youtube or Twitch links.
- Remote websites must be CORS/IFrame compatible with full SSL-encryption enabled.

## Join Room via WHIP

## Encoder information

WHIP URL HERE
- encoder settings here
- encoder settings here
- encoder settings here

## Run a Speed Test

## Custom Mixed Layouts

## Multi-Stream Monitor

## Podcast Studio

## Group Voice Comms

## Whiteboard

## Basic Usage Guides

## Wizard Link Generator

## Full Documentation

## Native Mobile Apps

## Source Code

## Show Your Support

## Publish via WHIP

## Share via WHEP

## Usage information

- WHEP sources are expected to support multiple viewers; simulcasting will be used if possible.
- Remote URLs must allows cross-origin requests (CORS), along with having SSL (https).

## If this page is unexpected, double check your links.

## What is VDO.Ninja

- 100% free ; no downloads; no personal data collection; no sign-in
- Bring live video from your smartphone, remote computer, or friends directly into OBS or other studio software.
- We use cutting edge Peer-to-Peer forwarding technology that offers privacy and ultra-low latency
- Youtube video Demoing it here
[LINK: Known issues:](https://docs.vdo.ninja/common-errors-and-known-issues/known-issues)
- If the video fails to load in OBS Studio, where the browser source remains blank, try disabling hardware-acceleration or refer to this help guide for more.
[LINK: refer to this help guide](https://docs.vdo.ninja/common-errors-and-known-issues/obs.ninja-doesnt-show-up-in-obs-or-is-choppy)
[LINK: changes here](https://github.com/steveseguin/vdo.ninja/commit/ee803984d4b1f7fc9174c4ddd92e172007150adc)

### 🛠 For support, join the Discord or see the sub-reddit . The documentation is here and my personal email is steve@seguin.email

[LINK: documentation is here](https://docs.vdo.ninja/)
[LINK: VDO.Ninja, by Steve Seguin](https://github.com/steveseguin/vdoninja)
[LINK: Terms of Service](https://docs.vdo.ninja/help/privacy-and-security-details/vdo.ninja-terms-of-service)
[LINK: Privacy Policy](https://docs.vdo.ninja/help/privacy-and-security-details/vdo.ninja-privacy-policy)
- A group room can handle up to around 30 guests, depending on numerous factors, including CPU and available bandwidth of all guests in the room. To achieve more than around 7-guests though, you will likely want to disable video sharing between guests . Using &broadcast, &roombitrate=0 or &novideo are options there.
- Videos will appear of low quality on purpose for guests and director; this is to save bandwidth and CPU resources. It will be high-quality within OBS still though.
- The state of the scenes, such as which videos are active in a scene, are lost when the director resets the control-room or the scene.
- Links to Solo-views of each guest video are offered under videos as they load. These can be used within an OBS Browser Source.
- You can use the auto-mixing Group Scenes, the green links, to auto arrange multiple videos for you in OBS.
- You can use this control room to record isolated video or audio streams, but it is an experimental feature still.
- If you transfer a guest from one room to another, they won't know which room they have been transferred to.
- OBS will see a guest's video in high-quality; the default video bitrate is 2500kbps. Setting higher bitrates will improve motion.
- VP8 is typically the default video codec, but using &codec=vp9 or &codec=h264 as a URL in OBS can help to reduce corrupted video puke issues.
- &stereo=2 can be added to guests to turn off audio effects, such as echo cancellation and noise-reduction.
- https://invite.cam is a free service provided that can help obfuscuate the URL parameters of an invite link given to guests.
- Adding &showonly=SOME_OBS_VIRTUALCAM to the guest invite links allows for only a single video to be seen by the guests; this can be output of the OBS Virtual Camera for example
[LINK: see the Wiki.](https://docs.vdo.ninja/advanced-settings)

## INVITE A GUEST

## CAPTURE A GROUP SCENE

## Guest 1

## Guest 2

## Guest 3

## Guest 4

Mix Order
Mix Order

### Change room settings

### Buffer Settings

### PTZ Controls

Keyboard Shortcuts:
Shift + Scroll = Pan
Ctrl / Cmd + Shift + Scroll = Tilt
Ctrl / Cmd + Scroll = Focus
Alt + Scroll = Zoom (fine)
Scroll = Zoom

### Publishing setup

### Remote Controller for OBS Studio

[LINK: documentation](https://docs.vdo.ninja/advanced-settings/upcoming-parameters/and-obs)

### Change guest settings

### Assign to slot:

[LINK: documentation](https://docs.vdo.ninja/advanced-settings)
- English
- German
- French
- Italian
- Spanish
- Polish
- Portuguese (Europe)
- Portuguese (Brazil)
- Dutch
- Turkish
- Japanese
- Arabic
- Chinese (中文)
- Czech
- Russian
- Ukrainian
- Basque
- Pig Latin
[LINK: Add More Here!](https://github.com/steveseguin/vdoninja/tree/master/translations)

--------------------