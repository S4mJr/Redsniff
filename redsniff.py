#
# RedSniff
# 
# Python Sniffer by S4m Jr
#
# Developer: Sam Junior
#
# Created for educational purposes
#
# ENJOY
#####################################
from core.build import *
from core.view import *
from scapy.all import *
from huepy import red
from os import geteuid

import os
import sys
import time


ban = '''\033[1;31m
████ ████    ██ ████       ██ ████ ████   
██   █  █    ██ ██            ██   ██      
██   ████ █████ ████ █████ ██ ████ ████                    
██   █    ██ ██   ██ ██ ██ ██ ██   ██   v1.0    
██   ████ █████ ████ ██ ██ ██ ██   ██
\033[m
Python Sniffer | By: S4m Jr
         t.me/SHI3LD
     github.com/S4mJr/Redsniff      

'''

if not geteuid() == 0:
    print(red(ban))
    exit('\033[1;31m[!] Redsniff must be run as root [!]\033[m\n\n[!] Example: sudo python3 redsniff.py [!]\n')

def run():
	clear()
	print(red(ban))
	main()

if __name__ == "__main__":
    try:
        run()                 
    except KeyboardInterrupt:
        end()
        sys.exit(0)
