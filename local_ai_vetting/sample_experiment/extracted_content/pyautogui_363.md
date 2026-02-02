# PyAutoGUI
**URL:** https://pyautogui.readthedocs.io/en/latest
**Page Title:** Welcome to PyAutoGUI’s documentation! — PyAutoGUI documentation
--------------------

- Docs »
- Welcome to PyAutoGUI’s documentation!
- Edit on GitHub
[LINK: Edit on GitHub](https://github.com/asweigart/pyautogui/blob/master/docs/index.rst)

## Welcome to PyAutoGUI’s documentation! ¶

PyAutoGUI lets your Python scripts control the mouse and keyboard to automate interactions with other applications. The API is designed to be simple. PyAutoGUI works on Windows, macOS, and Linux, and runs on Python 2 and 3.
To install with pip, run pip install pyautogui . See the Installation page for more details.
The source code is available on: https://github.com/asweigart/pyautogui
[LINK: https://github.com/asweigart/pyautogui](https://github.com/asweigart/pyautogui)
PyAutoGUI has several features:
- Moving the mouse and clicking in the windows of other applications.
- Sending keystrokes to applications (for example, to fill out forms).
- Take screenshots, and given an image (for example, of a button or checkbox), and find it on the screen.
- Locate an application’s window, and move, resize, maximize, minimize, or close it (Windows-only, currently).
- Display alert and message boxes.
Here’s a YouTube video of a bot automatically playing the game Sushi Go Round . The bot watches the game’s application window and searches for images of sushi orders. When it finds one, it clicks the ingredient buttons to make the sushi. It also clicks the phone in the game to order more ingredients as needed. The bot is completely autonomous and can finish all seven days of the game. This is the kind of automation that PyAutoGUI is capable of.

## Examples ¶

This example drags the mouse in a square spiral shape in MS Paint (or any graphics drawing program):
The benefit of using PyAutoGUI, as opposed to a script that directly generates the image file, is that you can use the brush tools that MS Paint provides.

## FAQ: Frequently Asked Questions ¶

Send questions to al @ inventwithpython . com
Q: Can PyAutoGUI work on Android, iOS, or tablet/smartphone apps.
A: Unfortunately no. PyAutoGUI only runs on Windows, macOS, and Linux.
Q: Does PyAutoGUI work on multi-monitor setups.
A: No, right now PyAutoGUI only handles the primary monitor.
Q: Does PyAutoGUI do OCR?
A: No, but this is a feature that’s on the roadmap.
Q: Can PyAutoGUI do keylogging, or detect if a key is currently pressed down?
A: No, PyAutoGUI cannot do this currently.

## Fail-Safes ¶

Like the enchanted brooms from the Sorcerer’s Apprentice programmed to keep filling (and then overfilling) the bath with water, a bug in your program could make it go out of control. It’s hard to use the mouse to close a program if the mouse cursor is moving around on its own.
As a safety feature, a fail-safe feature is enabled by default. When a PyAutoGUI function is called, if the mouse is in any of the four corners of the primary monitor, they will raise a pyautogui.FailSafeException . There is a one-tenth second delay after calling every PyAutoGUI functions to give the user time to slam the mouse into a corner to trigger the fail safe.
You can disable this failsafe by setting pyautogui.FAILSAFE = False . I HIGHLY RECOMMEND YOU DO NOT DISABLE THE FAILSAFE.
The tenth-second delay is set by the pyautogui.PAUSE setting, which is 0.1 by default. You can change this value. There is also a pyautogui.DARWIN_CATCH_UP_TIME setting which adds an additional delay on macOS after keyboard and mouse events, since the operating system appears to need a delay after PyAutoGUI issues these events. It is set to 0.01 by default, adding an additional hundredth-second delay.
Contents:
- Installation Windows macOS Linux
- Windows
- macOS
- Linux
- Cheat Sheet General Functions Fail-Safes Mouse Functions Keyboard Functions Message Box Functions Screenshot Functions
- General Functions
- Fail-Safes
- Mouse Functions
- Keyboard Functions
- Message Box Functions
- Screenshot Functions
- Mouse Control Functions The Screen and Mouse Position Mouse Movement Mouse Drags Tween / Easing Functions Mouse Clicks The mouseDown() and mouseUp() Functions Mouse Scrolling
- The Screen and Mouse Position
- Mouse Movement
- Mouse Drags
- Tween / Easing Functions
- Mouse Clicks
- The mouseDown() and mouseUp() Functions
- Mouse Scrolling
- Keyboard Control Functions The write() Function The press(), keyDown(), and keyUp() Functions The hold() Context Manager The hotkey() Function KEYBOARD_KEYS
- The write() Function
- The press(), keyDown(), and keyUp() Functions
- The hold() Context Manager
- The hotkey() Function
- KEYBOARD_KEYS
- Message Box Functions The alert() Function The confirm() Function The prompt() Function The password() Function
- The alert() Function
- The confirm() Function
- The prompt() Function
- The password() Function
- Screenshot Functions The screenshot() Function The Locate Functions
- The screenshot() Function
- The Locate Functions
- Testing Platforms Tested
- Platforms Tested
- Roadmap
- pyautogui pyautogui package
- pyautogui package
This documentation is still a work in progress.

## Indices and tables ¶

- Index
- Module Index
- Search Page

--------------------