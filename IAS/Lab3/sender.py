from scapy.all import *

def main():

    source_ip = input("Enter Source IP Address : ")
    source_port = int(input("Enter Source Port Address : "))

    destination_ip = input("Enter Destination IP Address : ")
    destination_port = int(input("Enter Source Port Address : "))

    print("Enter :\n1. To use sr() function\n2. To use sr1() function\n3. To use srloop()")
    option = int(input())

    packet = IP(src=source_ip, dst=destination_ip)/TCP(sport=source_port, dport=destination_port)
    
    if option==1:
    	sr(packet,timeout=10)
    elif option==2:
    	sr1(packet,timeout=10)
    elif option==3:
    	srloop(packet,timeout=10)


if __name__ == '__main__':
    main()
