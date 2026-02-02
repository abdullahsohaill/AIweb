# You need to set your browser to allow offline usage
**URL:** https://krpano.com/docu/localusage
**Page Title:** krpano.com - Documentation - Local / Offline Usage
--------------------


## Documentation

- Embedding
- XML Reference Textfield ScrollArea
- Textfield
- ScrollArea
- Actions / Scripting
- Javascript Interface
- Local / Offline Usage
- Coordinate Systems
- Release Notes

## Plugins

- Bing Maps
- Google Maps
- Gyro2
- krpano Maps
- Postprocessing
- Radar
- Snow / Rain
- Soundinterface
- ThreeJS
- Videoplayer
- WebVR

## XML Extensions

- controls3d.xml
- cursor3d.xml
- combobox.xml
- contextmenu.xml
- copy_to_clipboard.xml
- drag3d.xml
- measure3d.xml
- fps.xml
- ios_iframe_fullscreen.xml
- iphone_fullscreen_swipe.xml
- minimap_zoomrect.xml
- showtext.xml
- stateurls.xml
- vr_and_anaglyph_buttons.xml
- wakelock.xml
- webvr.xml
- webvr_autozoom.xml

## Tools

- Makepano Config File Reference
- Config File Reference
- Maketiles
- Makepreview
- SphereToCube
- CubeToSphere
- Protect Tool
- Encrypt Tool
- Registration Tool
- krpano Testing Server

## Third Party Software

- A list of third party software for krpano
- Your software here?

## Local / Offline Usage Version 1.23 Select Version: 1.23 1.22 1.21 1.20.12 1.20.11 1.20.10 1.20.9 1.20.8 1.20.7 1.20.6 1.20.5 1.20.4 1.20.2 1.20.1 1.20

- 1.23
- 1.22
- 1.21
- 1.20.12
- 1.20.11
- 1.20.10
- 1.20.9
- 1.20.8
- 1.20.7
- 1.20.6
- 1.20.5
- 1.20.4
- 1.20.2
- 1.20.1
- 1.20

## Solutions

- Using a localhost server (recommended)
- Changing the browser settings (not recommended)
- Building a standalone Desktop App (for end-user deployment)
- Embedding all files into the html file (only a special case for very small projects)

## Using a localhost server

## Changing the browser settings

- Firefox Before Firefox 68: Notthing todo in this case, that browser is allowing access to the local files in the same folder as the origin html file by default. For Firefox 68 and newer: Enter about:config in the browsers address bar. Then enter security.fileuri.strict_origin_policy in search bar on that config page
					to filter the available settings. Change that setting to false . After that access to local files should be possible, restarting the browser should be not necessary.

## Firefox

- Notthing todo in this case, that browser is allowing access to the local files in the same folder as the origin html file by default.
- Enter about:config in the browsers address bar.
- Then enter security.fileuri.strict_origin_policy in search bar on that config page
					to filter the available settings.
- Change that setting to false .
- After that access to local files should be possible, restarting the browser should be not necessary.
- Chrome Chrome would need to be started with --allow-file-access-from-files as argument.
			To do this: On Windows: Make a new shortcut/link icon to Chrome somewhere (e.g. by right-clicking it). Edit the proprieties of that new link (also by right-clicking it). Add --allow-file-access-from-files into the file path after Chrome.exe (make sure there is a blank between). Restart Chrome using that new icon (but make sure to close all currently opened Chrome windows before doing that). On Mac: Close all currently opened Chrome windows. Open the Terminal. Enter this line: open /Applications/Google\ Chrome.app --args --allow-file-access-from-files

## Chrome

- Make a new shortcut/link icon to Chrome somewhere (e.g. by right-clicking it).
- Edit the proprieties of that new link (also by right-clicking it).
- Add --allow-file-access-from-files into the file path after Chrome.exe (make sure there is a blank between).
- Restart Chrome using that new icon (but make sure to close all currently opened Chrome windows before doing that).
- Close all currently opened Chrome windows.
- Open the Terminal.
- Enter this line: open /Applications/Google\ Chrome.app --args --allow-file-access-from-files
- Safari (Mac) In the Safari Settings enable the Developer Menu in the Advanced tab. Then there will be a new Develop Menu in the Menubar. There enable the 'Disable Local File Restrictions' option.

## Safari (Mac)

- In the Safari Settings enable the Developer Menu in the Advanced tab.
- Then there will be a new Develop Menu in the Menubar.
- There enable the 'Disable Local File Restrictions' option.

## Building a standalone Desktop App

[LINK: NW.js](http://docs.nwjs.io/en/latest/For%20Users/Getting%20Started/)
- Download NW.js from here: https://nwjs.io/ .
- Extract it anywhere.
- As example: build a tour using the MAKE VTOUR droplet and copy the vtour folder into the extracted nwjs folder.
- Create a file named package.json inside the nwjs folder (any texteditor will do) with the following content: {"name":"My tour", "main":"vtour/tour.html"} This file tells NW.js which file to load when starting it.
- Then just click the nw.exe to start the tour.
- The nw.exe file could be also renamed to any other name.
- Download NW.js from here: https://nwjs.io/ .
- Right-click the nwjs application to show its package content.
- Go there first into the Contents and then into Resources folder.
- Make there a new folder named app.nw .
- As example: build a tour using the MAKE VTOUR droplet and copy the vtour folder into that app.nw folder.
- Create a file named package.json also inside the app.nw folder (any texteditor will do) with the following content: {"name":"My tour", "main":"vtour/tour.html"} This file tells NW.js which file to load when starting it.
- Then just click the nwjs to start the tour.
- The nwjs file could be also renamed to any other name.

## Embedding all files into the html file


--------------------