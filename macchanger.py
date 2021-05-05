import subprocess
import optparse
import re

def change_mac(interface,new_mac_address):

    subprocess.check_output(["ifconfig",interface,"down"])
    subprocess.check_output(["ifconfig",interface,"hw ether"+new_mac_address])
    command_output = subprocess.check_output(["ifconfig",interface,"up"])

    return re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(command_output))


def init_options():

    parser = optparse.OptionParser()

    parser.set_usage("macchanger.py -i <Interface> -m <MAC Address>")
    parser.add_option("-i","--interface",dest="interface",help="Interface to change it's MAC Address")
    parser.add_option("-m",dest="new_mac",help="New MAC Address")

    options,arguments = parser.parse_args()

    if options.interface == None:
        parser.error("An Interface MUST be introduced")
    elif options.new_mac == None:
        parser.error("A new MAC Address MUST be introduced")

    return options



user_data = init_options()

print("[+] Changing MAC address for "+user_data.interface+" ...")

new_mac_address = change_mac(user_data.interface, user_data.new_mac)

if (str(new_mac_address)==str(user_data.new_mac)):
    print("[+] Done. The new MAC Address is: "+str(new_mac_address))
