from scapy.all import *

def main():

    source_ip = '10.100.53.3'
    source_port = 12345
    destination_ip = '10.100.54.1'
    destination_port = 80

    packet = IP(src=source_ip, dst=destination_ip)/TCP(sport=source_port, dport=destination_port)
    unans, ans = sr(packet)


if __name__ == '__main__':
    main()
