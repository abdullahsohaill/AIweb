# Aircrack-ng
**URL:** https://www.kali.org/tools/aircrack-ng
**Page Title:** aircrack-ng | Kali Linux Tools
--------------------


## Tool Documentation:

## aircrack-ng Usage Examples

### WPA Wordlist Mode

Specify the wordlist to use ( -w password.lst ) and the path to the capture file ( wpa.cap ) containing at least one 4-way handshake.

### Basic WEP Cracking

To have aircrack-ng conduct a WEP key attack on a capture file, pass it the filename, either in .ivs or .cap/.pcap format:

## airgraph-ng Usage Examples

### CAPR graph

Specify the input file to use ( -i dump-01.csv ), the output file to generate ( -o capr.png ) and the graph type ( -g CAPR ):

### CPG graph

Specify the input file to use ( -i dump-01.csv ), the output file to generate ( -o cpg.png ) and the graph type ( -g CAG ):

## wpaclean Usage Example

Parse the provided capture files ( wpa-psk-linksys.cap wpa.cap ) and save any 4-way handshakes to a new file ( /root/handshakes.cap ):

## wesside-ng Usage Example

Use the specified monitor mode interface ( -i wlan0mon ) and target a single BSSID ( -v de:ad:be:ef:ca:fe ):

## makeivs-ng Usage Example

Specify a BSSID ( -b de:ad:be:ef:ca:fe ), WEP key ( -k 123456789ABCDEF123456789AB ), and output filename ( -w makeivs.ivs ):

## ivstools Usage Examples

Strip out the initialization vectors of the provided .pcap capture and save them to a new file:

## easside-ng Usage Example

First, run buddy-ng, then launch the Easside-ng attack, specifying as many of the options as you can.

## besside-ng

Attack WPA only ( -W ), display verbose output ( -v ) and use monitor mode interface wlan0mon .

## airtun-ng Usage Examples

### wIDS

Specify the BSSID of the access point you wish to monitor ( -a DE:AD:BE:EF:CA:FE ) and its WEP key ( -w 1234567890 ).

## airserv-ng Usage Example

Start a server instance on a specific port ( -p 4444 ) using the wlan0mon interface on channel 6 ( -c 6 ).

## airolib-ng Usage Examples

Specify the name of the database to use ( airolib-db ) and import a file containing the ESSIDs of the network(s) you are targeting ( –import essid /root/essid.txt ). If the database does not exist, it will be created.
Import any wordlists you wish to use for PMK computation.
Use the –batch to compute all PMKs.
To use the airolib-ng database with aircrack-ng, use the -r option and specify the database name.

## airodump-ng Usage Examples

Monitor all wireless networks, frequency hopping between all wireless channels.
Sniff on channel 6 (-c 6) via monitor mode interface wlan0mon and save the capture to a file (-w /root/chan6).
Filter for access points by a specific manufacturer, specifying the OUI and mask (-d FC:15:B4:00:00:00 -m FF:FF:FF:00:00:00).

## airodump-ng-oui-update Usage Example

airodump-ng-oui-update does not have any options. Run the command and wait for it to complete.

## airmon-ng Usage Examples

Entering the airmon-ng command without parameters will show the interfaces status.
A number of processes can interfere with Airmon-ng. Using the check option will display any processes that might be troublesome and the check kill option will kill them for you.
Enable monitor mode (start) on the given wireless interface ( wlan0 ), fixed on channel 6 . A new interface will be created ( wlan0mon in our case), which is the interface name you will need to use in other applications.
The stop option will destroy the monitor mode interface and place the wireless interface back into managed mode.

## airgraph-ng Usage Examples

### CAPR graph

Specify the input file to use ( -i dump-01.csv ), the output file to generate ( -o capr.png ) and the graph type ( -g CAPR ).

### CPG graph

Specify the input file to use ( -i dump-01.csv ), the output file to generate ( -o cpg.png ) and the graph type ( -g CAG ).

## aireplay-ng Usage Examples

### Injection Test

Run the injection test ( -9 ) via the monitor mode interface wlan0mon .

### Deauthentication Attack

Run the deauthentication attack ( -0 ), sending 5 packets to the wireless access point ( -a 8C:7F:3B:7E:81:B6 ) to deauthenticate a wireless client ( -c 00:08:22:B9:41:A1 ) via the monitor mode interface wlan0mon .

### Fake Authentication

Run the fake authentication attack and re-authenticate every 6000 seconds ( -1 6000 ) against the access point ( -a F0:F2:49:82:DF:3B ) with the given ESSID ( -e FBI-Van-24 ), specifying our mac address ( -h 3c:46:d8:4e:ef:aa ), using monitor mode interface wlan0mon .

## airbase-ng Usage Examples

### Hirte Attack – Access Point Mode

The Hirte attack attempts to retrieve a WEP key via a client. This example creates an access point on channel 6 ( -c 6 ) with the specified ESSID ( -e TotallyNotATrap ) and uses the cfrag WEP attack ( -N ), setting the WEP flag in the beacons ( -W 1 ).

### Caffe Latte Attack – Access Point Mode

As with the Hirte attack, the Caffe Latte Attack attempts to retrieve a WEP key via a client. This example creates an access point on channel 6 ( -c 6 ) with the specified ESSID ( -e AlsoNotATrap ) and uses the Caffe Latte WEP attack ( -L ), setting the WEP flag in the beacons ( -W 1 ).

## airdecap-ng

With a given ESSID ( -e test ) and password ( -p biscotte ), decrypt the specified WPA capture ( -r /usr/share/doc/aircrack-ng/examples/wpa.cap ).

## Packages and Binaries:

### aircrack-ng

Wireless WEP/WPA cracking utilities aircrack-ng is an 802.11a/b/g WEP/WPA cracking program that can recover a
40-bit, 104-bit, 256-bit or 512-bit WEP key once enough encrypted packets
have been gathered. Also it can attack WPA1/2 networks with some advanced
methods or simply by brute force.
It implements the standard FMS attack along with some optimizations,
thus making the attack much faster compared to other WEP cracking tools.
It can also fully use a multiprocessor system to its full power in order
to speed up the cracking process.
aircrack-ng is a fork of aircrack, as that project has been stopped by
the upstream maintainer.
Installed size: 2.46 MB How to install: sudo apt install aircrack-ng
- ethtool
- hwloc
- libc6
- libgcc-s1
- libhwloc15
- libnl-3-200
- libnl-genl-3-200
- libpcap0.8t64
- libpcre2-8-0
- libsqlite3-0
- libssl3t64
- libstdc++6
- python3
- rfkill
- usbutils
- wireless-tools
- zlib1g
Multi-purpose tool aimed at attacking clients as opposed to the Access Point (AP) itself
A 802.11 WEP / WPA-PSK key cracker
Decrypt a WEP/WPA encrypted pcap file
Removes wep cloaked framed from a pcap file.
Inject packets into a wireless network to generate traffic
POSIX sh script designed to turn wireless cards into monitor mode.
A wireless packet capture tool for aircrack-ng
IEEE oui list updater for airodump-ng
Manage and create a WPA/WPA2 pre-computed hashes tables
A wireless card server
A virtual tunnel interface creator for aircrack-ng
Encrypted WiFi packet injection
Crack a WEP or WPA key without user intervention and collaborate with WPA cracking statistics
Filter EAPOL frames from a directory of capture files.
A tool to work with easside-ng
An auto-magic tool which allows you to communicate via an WEP-encrypted AP without knowing the key
Extract IVs from a pcap file or merges several .ivs files into one
Show statistical FMS algorithm votes for an ivs dump and a specified WEP key
Generate a dummy IVS dump file with a specific WEP key
Forge packets: ARP, UDP, ICMP or custom packets.
Inject a few frames into a WPA TKIP network with QoS
Crack a WEP key of an open network without user intervention
Clean wpa capture files

### airgraph-ng

Tool to graph txt files created by aircrack-ng airgraph-ng is a tool to create a graph ouf of the txt file created by airodump
with its -w option. The graph shows the relationships between the clients and
the access points.
Installed size: 99 KB How to install: sudo apt install airgraph-ng
- graphviz
- python3
A 802.11 visualization utility
A support tool for airgraph-ng that allows you to join the airodump output files.

## Learn more with OffSec

Want to learn more about aircrack-ng? get access to in-depth training and hands-on labs:
- PEN-210: 6. Aircrack-ng Essentials
PEN-210 course
Updated on: 2025-Dec-09

--------------------