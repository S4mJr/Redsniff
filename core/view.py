from core.build import *
import platform
from os import system
from huepy import red

so = platform.system()

def main():
	print("[S] MITM\n[A] Arping")
	option = str(input("\nRS > "))
	if option == 'S':
			mitm()
	if option == 'A':
			arping()

def clear():
	os.system("clear")						

fin = '''
RED SNIFF                 Created
Python Sniffer Tool           For
By: ReverseTeam          Educational Purpose
'''

def end():
	system('clear')
	print(red(fin))
	print("\nOS:     \t"+so)
	print("\nMachine:\t"+platform.machine())
	print("\nPC-Name:\t"+platform.node())	
	print("\nPlataform:\t"+platform.platform())
	print("")
