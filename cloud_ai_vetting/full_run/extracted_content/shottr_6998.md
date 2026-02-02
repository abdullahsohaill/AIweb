# Shottr
**URL:** https://shottr.cc
**Page Title:** Shottr – Screenshot Annotation App For Mac
--------------------


## Screenshot tool for

## designers

## front-end engineers

## mobile developers

## those who care about pixels

### Designed to be lightweight

Shottr is a tiny (2.3mb dmg) native app optimized for Apple Silicon. It takes only 17ms to grab a screenshot, and ~165ms to show it to you.

### Beautiful Backgrounds

Make your screenshots stand out with gradients backgrounds, shadows and rounded corners.

### Scrolling Screenshots on Mac

Take a screenshot of a long web page or capture conversation in a chat. Any app, any window.

### Pixelate or remove objects

Hide parts of your screen behind pixelated curtain, or remove sensitive information as if it was never there. Text mode hides text without corrupting anything else.

### Text recognition (OCR) & QR

Came by a text that won’t select? Press a hotkey and select an area — Shottr will parse the text and copy it to the clipboard. OCR feature also reads QR codes.

### Combine Screenshots

Take multiple screenshots and put them on the same canvas using the Add Capture button on the toolbar.

### Resize Screenshots

Make your screenshots bigger or smaller, right in the app (click on the image size in the upper right corner).

### Pin Screenshots

Pin images as floating always-on top borderless windows. Convenient for keeping references, or as a temporary screenshots storage.

### Markup screenshots

Add text, freehand drawings, highlights, spotlights and other visual effects to your drawings.

### Overlay Images

Paste images on top of your screenshots. Make overlays semi-transparent to highlight the differences, or generate two-frame before/after animations.

### Use it as a Screen Ruler

Press ↑ or ↓ key and move your mouse to measure vertical size, ← or → for horizontal size. Click to imprint the measurement on the screenshot.

### Unclutter your desktop

Select a dedicated folder to save screenshots on ⌘ s . Great for purchase receipts, reminders, archive items, random images, etc.

### Zoom in on your pixels

Think of Shottr as your digital magnifying glass. If you need to have a closer look at something, take a screenshot and zoom in.

### Color picker

Take a screenshot, zoom in, move your mouse over the pixel and press the TAB key to copy color under the cursor.

## What feature should I build next?

(Check the Feature Request Form for the other popular requests)

## Get Shottr Updates

Don't worry, I'm too lazy for spam

## Tips and Tricks

### Quick zoom on the selection

Press cmd + 2 to quickly zoom on the selected region. Other helpful shortcuts: Q – Zoom on the top left corner of the selection. W – Zoom on the bottom right corner of the selection. cmd + 1 – Zoom to fit. cmd + 0 – Zoom to 100%. cmd + + / – – Zoom in / out.

### Crop the image

Just select the area you would like to crop and hit Enter . It's that simple!

### Quickly select monotone objects

If you want to select a monotone object, to check its size or to crop it, hold ⌘ and click on it.

### Smart selection mode

Press A after you selected an area to auto-adjust selection.
				Hold ⌥ while selecting to see the instant preview of what the selection will adjust to.

### Copy text color

Move your mouse over a line of text and press Shift + TAB . No need to be precise, the darkest pixel of the 20×20px area will be copied.

### Copy average color

Select an area and press C to copy average color of the area.

### Measuring objects on retina display

All sizes on Retina screens are measured in logical (non-retina) pixels. If you want to see sizes in physical (retina) pixels, click on the dimension box at the top right corner.

### How to enlarge the screenshot

- Make a screenshot.
- Zoom in.
- Make a screenshot of the zoomed area.
- Crop.

### Quick zoom in

Press Z and click on the screenshot – Shottr will zoom in on that spot.

### Pan with the mouse

Drag with the right mouse button to move the screenshot around. You can also press Space and use the left button.

### Manipulate selection with the keyboard

Arrows – Nudge selection (1px) Shift + Arrows – Nudge (10px) Cmd + Arrows – Resize (1px) Cmd + Shift + Arrows – Resize (10px) [ , ] – Enlarge selection by 1px on each side. Shift + [ , ] – Enlarge by 10px.

### Measure distance between objects

Move your mouse in between two objects on a screenshot and press an arrow key – left or right for horizontal distance, up or down for vertical.

## Frequently Asked Questions

### Is Shottr free?

### Can Shottr upload the image online and copy link?

### Which macOS versions are supported?

### When and why does Shottr contact Shottr.cc?

[LINK: https://shottr.cc/api/version.json](https://shottr.cc/api/version.json)

## Release Notes

- Expanded support for third-party S3 services (Tencent, Yandex, Minio, etc).
- Print dialog now allows changing print orientation.
- Freehand tool: brought back an ability to draw a point with a single click.
- Aesthetic adjustments to both hand-drawn and classic rectangle styles.
- Bug fix: the app used to show the editor along with the preview thumbnail when macOS failed to grant the permission to activate the app.
- Bug fix: S3 upload on the systems with non-gregorian calendar.
- Bug fix: app freezing on affected computers.
- S3 Upload (any S3-compatible storage).
- Magnifier tool (zoomed-in callout).
- Hand-drawn style option for Text, Arrow, Oval and Rectangle objects.
- Every arrow type can now be bent in an arch.
- Configurable object snapping (check the Draw menu).
- All 16 tools are now shown in the toolbar if the window is large enough.
- Custom-styled Notification could now be dismissed by dragging it out (drag up).
- Menubar icon shows a quick confirmation animation when copying, saving or uploading files.
- Copy to clipboard may have had a delay on busy computers. Not anymore.
- The option to prefer large window had an issue in v1.8. It's fixed now, and renamed to Default zoom level: Prefer 100%.
- On the computers affected by macOS scrolling capture issue, the app should deploy a workaround.
- Shottr now uses a workaround when macOS blocks its request to activate on hotkey.
- Fixed a rare crash in the auto-adjust feature when the selection touches the lower edge of the image.
- OCR prevents accidental appearance of double spaces in the output.
- Backdrop tool: Shadows rendering algorithm was tweaked to produce a neater shadow for smaller intensity values.
- Added OKLCH to the list of available colors in the color inspector
- Added APCA measurement to the color contrast checker (switch between the WCGA 2.0 and APCA by Opt+Click on the contrast value)
- Fixed a bug when the previous image would occasionally stay in the clipboard after Cmd+C or Esc.
- Fixed a bug when the large (a few megapixel) backdrop would take a long time to render on Save or Copy.
- If on your computer Cmd+Z affects more than one text object at once, that bug is now fixed.
- Backdrop Tool
- Support for Raycast Extension and Alfred Workflow
- URL Schemes API: more info
- Custom annotation colors
- More sizes for Text labels, Arrows, and other annotations
- Setting to hide the splash screen
- Better handling of thumbnails on top of the Fullscreen windows
- Numerous smaller improvements and fixes
- Freehand Drawing tool (change stroke variability with cmd+enter, smoothness with opt+up/down)
- Text Highlighter tool (change cap style with cmd+enter)
- Spotlight tool (change background opacity with keys 1..9)
- Image resizer (click on the image size in the upper right corner)
- An option to hide the menubar icon (only available with the license)
- A button to remove linebreaks from the OCR text after it was recognized, and a setting to remove
						linebreaks by default
- Fixed an issue when scrolling capture would include a cursor in the middle of the screenshot on some
						computers
- Scroll Capture will show a message if it fails to scroll, or if it reaches the max-height limit
- A setting to reverse auto-scroll direction (may help if you're using an app like Scroll Reverser)
- Ability to blur selected area by pressing key B
- The editor window now always opens on the screen on which the screenshot was taken
- Holding Shift while selecting the image area will produce a square selection
- Starting the app when it's already running will bring the original app forward instead of showing the
						message
- If your Shottr icon is pinned in the dock, clicking on it when the app is running but the window is
						closed will open up the editor
- Semi-transparent pinned screenshot doesn't have a shadow now. Convenient for overlay comparison.
- Fixed a bug when the Max Scrolling Height won't persist after the app relaunch
- Auto-update functionality
- Preview thumbnail now opens on top of the Fullscreen and Stage Manager windows
- Added fill/opacity control to the  Rectangle and Oval instruments
- Pinned screenshots can be resized with scroll
- New editor shortcuts: Cmd+Shift+O to open a file, and Cmd+Shift+V to load image from the clipboard
- Save As shortcut (Cmd+Shift+S) now works in the preview thumbnail as well
- When you selected an annotation object, it goes to the frontmost level, on top of other drawings
- Size slider changes objects in real-time
- BUG Fix: text editing and resizing now works properly on all zoom levels
- Fixed an issue when a part of the mouse cursor would show up in the corner of the area-capture screenshot
- Automatic filename timecode changed from alphanumeric to alphabetic, files will now be properly chronologically sorted when sorting by name in Finder
- A setting to keep the preview thumbnail up until you use the image, or close the thumbnail.
- Ability to assign hotkeys to "Capture Any Window" and "Reopen Shottr" actions.
- A button to quickly add padding to selection marquee (convinient after applying Autoadjust):
- Click on a selection marquee edge to auto-adjust this edge only.
- Fixed a bug when Pinned screenshot will display at 50% on low-dpi displays.
- Some clipboard managers used to miss certain screenshots copied by Shottr. This should not be happening any more.
- Saving retina images with 144dpi when applicable.
- A more prominent notification about the new version.
- If you drag-and-drop image onto the app like Yoink or Dropover, the file will remain available after the new screenshot is done.
- Increased max scrolling screenshot height limit to 200,000px (it's still set to 20,000px by default).
- Pin screenshots: ability to pin the image as a floating always-on-top window.
- Image overlay: paste images on top of the screenshot.
- Before/after gifs. Quickly create two-frame animations (paste an "after" image on top of the "before" screengrab, press "5" to enable transpaency, align frames and hit the GIF icon in the top right corner of the app):
- Custom confirmations for OCR, Color Copy, Save and Upload, and an option to turn off notifications completely. System notifications are available in the app settings, but they will only work if Shottr is allowed to show them (System Preferences → Notifications)
- Added customizable shortcut for the Repeat Area capture.
- More robust DPI detection when working with Retina and Non-retina monitors at the same time.
- Undo/Redo now available from the menu as well.
- Improved Text-only erase and pixelation accuracy for Chinese.
- Fixes Text label rendering bug intrpduced by macOS Ventura Beta 4.
- Added Step counter annotation tool
- Text-only mode for Blur/Erase tool
- Opt+Drag to duplicate drawings
- Ability to manage uploaded Screenshots (main menu button)
- Bug fix: crash with auto-copy/auto-save settings
- More robust Undo functionality
- Now Shottr copies PNG instead of TIFF on Esc or Cmd+C
- Shottr keeps selected tool after the object is created (it's quicker now to add multiple arrows, counters, etc.)
- Object attributes panel doesn't hide the tool selector
- Default instrument (Select/Crop) now has a button and a shortcut (V)
- Text label has a pointy arrow by default
- Cmd+V and Cmd+D insertion position is more predictable now
- A setting to automatically Copy and/or Save the image after screenshot.
- A setting to show Preview instead of the Editor after the Area Capture.
- Quick zoom by Z+Drag (press Z and drag your mouse around the area that you want to zoom in).
- Ability to open files and load clipboard images from the main menu (Shottr icon → More → Open File.)
- Hold CMD while drawing an arrow to reverse its deirection
- When part of the image is selected, Cmd+C now copies the selection only, and doesn’t close the window.
- Drag’n’drop now applies the same settings as regular save (PNG/Jpeg, 1x downscale).
- Default Folder selection dialogue allows to create New Folder.
- More robust checking for Screen Recording permissions.
- Bug fix: Scrolling Capture now works fine when the Hot Corners are enabled.
- Bug fix: Cmd+C used to rely on the Esc button settings.
- Ability to change object styling (color, thickness, line style, pixelation level, etc)
- Setting to change behavior of the Escape button when nothing is selected (options to Copy image and/or Save image)
- Setting to open Shottr window bigger by default. When selected, the app starts at 80% zoom for the fullscreen screenshot, and area screenshots will open at 100% zoom more often
- Setting to turn on/off telemetry collection. Please consider leaving this checkbox on, at least for a while, so that I can verify the app runs smoothly and no exceptions are thrown across variety of devices and OS versions
- Ability to open a PNG or Jpeg file in Shottr via the “Open With” context menu. The app needs to be copied to the Application folder for that feature to work. If you save the opened file, it will override the original file
- You can also open the image file through the “File” → “Open File” menu item
- QR Reader: Text Recognition now detects and decodes QR codes
- Guides: hold Opt+S or Opt+D to show a vertical or horizontal guide, click to imprint it on the image
- Cmd+C / Cmd+V now works for the annotation objects
- Chinese language is supported in Text Recognition. You need to select Chinese as your primary language in the Preferences (Advanced tab)
- Added Repeat Area Screenshot – it will retake screenshot of the previously selected area
- Added Delayed Screenshot (3s delay)
- Arrow tool improvements. Longer arrows are now slimmer, more styles are available, including curved arrows and super-slim arrows.
- Hold space while drawing an object to move it around.
- If you start taking an area capture and hit Esc in the process, the window won’t pop up.
- Pixelation algo produces a more uniform pattern, works a tad faster too.
- Pixelation on small areas scrambles pixels for better protection.
- Improved Ruler rendering on non-retina displays (crisper look).
- Window screenshot with Wallpaper or Solid background now have proportionate top and bottom paddings.
- Addressed an issue when the cursor is occasionally imprinted in the scrolling screenshot.
- Cosmetic improvements to the object handling knobs and helper popovers.
- Added new color format: HEX without the sharp (#) character.
- Improved stability when doing Cmd+Click raster selection on area screenshots.
- Window Screenshot better process edge case scenarios and allows you to select window is Shottr can’t identify which window is currently active.
- Scrolling Capture (up and down)
- Area capture
- Active window capture
- Instant text recognition
- Objects Removal (selection + Delete)
- Hotkeys customization
- Window Capture modes: keep shadow on a transparent background, trim window shadow, keep shadow on a solid background, keep shadow over a wallpaper
- Color format setting (click on the current pixel color box in the toolbar)
- Auto format selection setting for Cmd+S: Shottr will save images with lots of text as PNG and choose JPEG if the screenshot is graphic-heavy
- A setting to keep the main window always on top
- Cmd+Z / Cmd+Shift+Z for Undo/Redo
- Menu "Edit" → "Reset Crop" undoes cropping
- Hitting Tab while editing text label will add color under the cursor to the label’s text
- The main window is now resizable and supports fullscreen
- Ability to drag’n’drop file on the main window canvas to open an image
- If you’re using multiple spaces,  the main window will now open in the active space
- Trackpad and Magic Mouse zoom is smoother
- Cmd+Q now shows a dialog asking if the app should close or quit, the selection is remembered
- Shottr remembers OS permissions to access the selected screenshots folder and doesn’t ask for permissions after each restart

## Thank you for choosing Shottr

Shottr depends on user support, help me to spread the word!

## Pay what you want

Name your price, or enter $0 to get Shottr for free

--------------------