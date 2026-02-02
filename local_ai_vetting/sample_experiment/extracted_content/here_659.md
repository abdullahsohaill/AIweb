# here
**URL:** https://www.chromium.org/developers/how-tos/run-chromium-with-flags
**Page Title:** Run Chromium with command-line switches
--------------------

[LINK: For Developers](/developers)
[LINK: How-Tos](/developers/how-tos)

## Run Chromium with command-line switches

There are command-line switches that Chromium (and Chrome) accept in order
to enable particular features or modify otherwise default functionality.
There is no list of all switches, but most of the existing switches
can be found at https://peter.sh/examples/?/chromium-switches.html .
Note : Chrome switches (e.g., --incognito )
and Chrome flags (e.g., chrome://flags/#ignore-gpu-blocklist ) are separate configurations.
Some features can be enabled by a command-line switch, flag or both.
[LINK: Chrome switches](https://chromium.googlesource.com/chromium/src/+/main/docs/configuration.md#switches)
[LINK: Chrome flags](https://chromium.googlesource.com/chromium/src/+/main/docs/configuration.md#flags)
It is important to note that some switches are intended for development and
temporary cases. They may break, change, or be removed in the future without
notice. IT admins looking to manage Chrome for their organization should
instead use enterprise policies .
Note that if you look at chrome://flags to see if the command-line option is
active, the state might not be accurately reflected. Check chrome://version for the complete command-line used in the current instance.

## Windows

- Exit any running-instance of Chrome (e.g., navigate to chrome://quit ).
- Right click on your "Chrome" shortcut.
- Choose properties.
- At the end of your "Target:" line add the command-line switch. For
example: --disable-gpu-vsync
- --disable-gpu-vsync
- With that example flag, it should look like below (replacing
"--disable-gpu-vsync" with any other command-line switch you want to
use): chrome.exe --disable-gpu-vsync
- Launch Chrome like normal with the shortcut.

## macOS

- Quit any running instance of Chrome (by navigating to chrome://quit ).
Quit any running instance of Chrome (by navigating to chrome://quit ).
- Run your favorite Terminal application.
Run your favorite Terminal application.
- In the terminal, run commands like below (replacing
"--remote-debugging-port=9222" with any other command-line switch you
want to use): /Applications/Chromium.app/Contents/MacOS/Chromium --remote-debugging-port=9222
# For Google Chrome you'll need to escape spaces like so:
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
In the terminal, run commands like below (replacing
"--remote-debugging-port=9222" with any other command-line switch you
want to use):

## Linux

- Quit any running instance of Chrome (e.g., navigate to chrome://quit ).
Quit any running instance of Chrome (e.g., navigate to chrome://quit ).
- Run your favorite terminal emulator.
Run your favorite terminal emulator.
- In the terminal, run commands like below (replacing
"--remote-debugging-port=9222" with any other command-line switch you
want to use): chromium-browser --remote-debugging-port=9222
google-chrome --foo --bar=2
In the terminal, run commands like below (replacing
"--remote-debugging-port=9222" with any other command-line switch you
want to use):

## iOS

If you are building Chromium from the source, you can run it with command-line
switches by adding them in the Experimental Settings.
- Open the Settings app
- Go to Chromium/Experimental Settings
- Add your switches in the "Extra flags (one per line)". Don't forget to
switch on the "Append Extra Flags" setting.
It is not possible to run with flags the official releases (Google Chrome from
App Store or Testflight).

## V8 Flags

V8 can take a number of flags (command-line switches) as well,
via Chrome's js-flags flag. For example, this traces V8 optimizations:
To get a listing of all possible V8 flags:
Browse the V8 docs for more flags for V8.
[LINK: the V8 docs](https://v8.dev/docs)

## Android

Visit about:version to review the command-line switches that are effective
in the app.
If you are running on a rooted device or using a debug build of Chromium, then
you can set switches like so:
You can also install, set switches, and launch with a single command:
For production build on a non-rooted device, you need to enable "Enable command
line on non-rooted devices" in chrome://flags, then set command-line in
/data/local/tmp/chrome-command-line. When doing that, mind that the first
command-line item should be a "_" (underscore) followed by the ones you actually
need. Finally, manually restart Chrome ("Relaunch" from chrome://flags page
might no be enough to trigger reading this file). See https://crbug.com/784947 for more information. To set the flags without having
a production build, adb can be used instead by following these instructions from the WebView docs (but note that the file path mentioned above should be
used instead of the WebView-specific path shown there).
[LINK: these instructions](https://chromium.googlesource.com/chromium/src/+/main/android_webview/docs/commandline-flags.md#manual)

### ContentShell on Android

There's an alternative method for setting command-line switches with ContentShell
that doesn't require building yourself:
- Download a LKGR build of
Android .
- This will include both ChromePublic.apk and ContentShell.apk
- Install ContentShell APK to your device.
- Run this magic incantation
This will launch contentshell with the supplied switches. You can apply whatever
commandLineArgs you want in that syntax.

### Android WebView

This is documented in the chromium
tree .
[LINK: in the chromium
tree](https://chromium.googlesource.com/chromium/src/+/HEAD/android_webview/docs/commandline-flags.md)

## Chrome OS

- Put the device into dev mode, disable rootfs verification, and
bring up a command
prompt .
[LINK: dev mode, disable rootfs verification, and
bring up a command
prompt](/chromium-os/developer-library/guides/device/developer-mode/)
- Modify /etc/chrome_dev.conf (read the comments in the file for more
details).
- Restart the UI via: sudo restart ui

--------------------