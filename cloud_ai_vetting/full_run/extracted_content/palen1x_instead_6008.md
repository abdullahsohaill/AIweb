# Palen1x instead
**URL:** https://ios.cfw.guide/using-palen1x
**Page Title:** Using palen1x | iOS Guide
--------------------


## Using palen1x

DANGER
If you are trying to use a Virtual Machine software of some sort from Windows (e.g. Virtualbox, VMWare, Windows Subsystem for Linux, etc) you will not succeed with following this guide, and will need to obtain a bootable medium and follow the below steps using that bootable medium.
WARNING
If you are using a computer with an AMD Ryzen CPU, you will likely run into issues. If you do run into issues, you should use a Mac or a computer with an Intel CPU to follow this guide.
palen1x is a live bootable Linux environment that allows you to quickly run palera1n on a compatible device. palera1n is capable of jailbreaking iOS devices with A8(X) to A11 SoC's on iOS 15.0 and later.
On A11 devices, you must disable your passcode and will not be able to use your passcode, or other SEP functionality, until you boot into a stock iOS state. SEP functionality includes things such as a passcode, Face ID/Touch ID, and Apple Pay.
Additionally, if your device is an A11 device on iOS 16 and you've set a passcode before, you will need to erase all content and settings in order to be able to jailbreak.

## # Requirements

- A 128MB or greater USB Drive If you don't have a USB Drive, but do have another form of supported removable bootable hardware (e.g. A CD or DVD), you can use that instead of a USB Drive
- If you don't have a USB Drive, but do have another form of supported removable bootable hardware (e.g. A CD or DVD), you can use that instead of a USB Drive
- The latest version of palen1x Open in new window
[LINK: palen1x Open in new window](https://github.com/palera1n/palen1x/releases)
- Ventoy Open in new window
[LINK: Ventoy Open in new window](https://github.com/ventoy/Ventoy/releases)

## # Installing Ventoy

- Download and extract the contents of the Ventoy.zip file
- Insert your USB drive if you have not already done so, and open the Ventoy2Disk.exe file
- Select the USB drive you would like to boot palen1x from This USB drive will be completely erased Ensure you back up all important data beforehand
- This USB drive will be completely erased
- Ensure you back up all important data beforehand
- Click Install and confirm that you are ok erasing the USB drive Do not remove your USB Drive until the process has completed
- Do not remove your USB Drive until the process has completed
- Once it has installed, copy the palen1x iso file that you downloaded onto the USB drive

## # Booting palen1x

- Reboot, and then go into your BIOS settings and disable Secure Boot, then enter the boot picker and select your USB Drive to boot from This is different for every computer Search your PC or motherboard brand to find out how to get to your BIOS settings if you are unsure
- This is different for every computer
- Search your PC or motherboard brand to find out how to get to your BIOS settings if you are unsure
- Press enter once you see the Ventoy screen to boot into palen1x

## # Running palera1n

WARNING
If you are using a USB-C to Lightning cable to do this process, you may run into issues entering into DFU mode
If you do have issues, get a USB-A to Lightning cable and, if necessary, also get a USB-C to USB-A adapter.
- Once you have loaded palen1x, select Shell
- Type palera1n -l
- Follow the on screen instructions to enter DFU mode .
TIP
A9(X) and earlier devices have an issue where they will get stuck midway through this process in pongoOS. To work around this issue, you'll need to do the following:
- In the terminal window, press Control + C on your keyboard
- Rerun the command that you just ran
You'll need to do this every time you rejailbreak your device as well.
Once the device boots up, open the palera1n loader app and tap Sileo . After a bit of time, you'll be prompted to set a passcode for using command line stuff, and then afterwards, Sileo should be on your home screen.
TIP
To rejailbreak your device, simply rerun the command you just ran and then repeat any other applicable steps.
Alternatively, if you're on versions 15.0 to 16.6.1, you can follow Installing Dopamine to install a permanently signed semi-untethered jailbreak, which will allow you to rejailbreak your device without a computer.

--------------------