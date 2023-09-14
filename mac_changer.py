#!/usr/bin/env python

import subprocess
import optparse
import random

new_mac = ["00:0c:29:a6:d0:a5", "22:11:33:35:d5:00", "00:0d:3d:35:d5:00", "54:0d:3d:35:d5:00"]

new_address = random.choice(new_mac)

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    (option, arguments) = parser.parse_args()
    if not option.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    return option


def change_mac(interface, new_address):
    print(f"[+] Changing Mac Address for {interface} to {new_address}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_address])
    subprocess.call(["ifconfig", interface, "up"])

option = get_arguments()
change_mac(option.interface, new_address)