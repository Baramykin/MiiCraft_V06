#!/usr/bin/env python
#
# -*- coding: utf-8 -*-
#
import platform
import subprocess
import sys


# Select windows platform, 32bits or 64 bits
def selectDevcon():
    arch = platform.architecture()
    processor = platform.processor()
    is_amd = processor.find('AMD')
    if is_amd < 0:
      is_amd = processor.find('amd')
    
    if arch[0] == "32bit":
        devcon_path = "devcon32.exe"
    elif is_amd == 0:
        devcon_path = "devcon64a.exe"
    else:
        devcon_path = "devcon64i.exe"
    return devcon_path


# Disable Arduino Mega 2560
def restartDevice():
    ARDUINO_ID = "*USB\VID_2341*PID_0042*"
    devcon_path = selectDevcon()
    cmd = "%s disable %s" % (devcon_path, ARDUINO_ID)
    subprocess.call(cmd, shell=True)
    cmd = "%s enable %s" % (devcon_path,  ARDUINO_ID)
    subprocess.call(cmd, shell=True)


if __name__ == '__main__':
    restartDevice()
    sys.exit()
