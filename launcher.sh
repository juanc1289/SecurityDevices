#!/bin/sh
# launcher.sh
# navigate home, then to the directory, then execute the python script 
#[sudo python gps3_powerkey.py ]
#[sudo python camera4_video_loop.py]

cd /
cd home/juanc/Desktop/git/SecurityDevices/
sleep 6 && lxterminal -e sudo python gps3_powerkey.py && lxterminal -e sudo python camera4_video_loop.py
