from scapy.all import *

import pandas as pd
import numpy as np
import math


def acl_rule_extractor():
    acl_rules = pd.read_excel('ACL-File.xlsx', na_values=[]).fillna(-1).values

    num_rules = 0
    num_cols = acl_rules.shape[1]

    for i in range(acl_rules.shape[0]):
        flag = 1
        for j in range(acl_rules.shape[1]):
            if acl_rules[i][j] == -1:
                flag = 0
                break

        if flag == 1:
            num_rules = num_rules + 1

    acl_rules = acl_rules[:num_rules, :]

    return acl_rules


def hexdump_parser(dataset, acl_rules, filename):
    data = list(map(lambda x: int(x, 16), dataset.split()))

    mac_addr = dict()
    mac_addr['dest'] = dataset.split()[0:6]
    mac_addr['src'] = dataset.split()[6:12]

    print('Source MAC Address:', ":".join(map(str, mac_addr['src'])), file=open(filename, "a+"))
    print('Destination MAC Address:', ":".join(map(str, mac_addr['dest'])), file=open(filename, "a+"))

    etherType = data[12:14]

    packet_type = ""

    # IPv4 Packet
    if etherType[0] == 8 and etherType[1] == 0:

        print('Packet Type: IPv4', file=open(filename, "a+"))

        ipVersion = data[14] > 4

        protocol_num = data[23]
        protocol = ''

        if protocol_num == 6:
            protocol = 'TCP'
        elif protocol_num == 17:
            protocol = 'UDP'

        print('IPv4 Packet Protocol:', protocol, file=open(filename, "a+"))

        ip_addr = dict()

        ip_addr['src'] = data[26:30]
        ip_addr['dest'] = data[30:34]

        port_num = dict()
        port_num['src'] = (data[34] << 8) + data[35]
        port_num['dest'] = (data[36] << 8) + data[37]

        print('Source IP Address:', ".".join(map(str, ip_addr['src'])), file=open(filename, "a+"))
        print('Source IP Port:', port_num['src'], file=open(filename, "a+"))
        print('Destination IP Address:', ".".join(map(str, ip_addr['dest'])), file=open(filename, "a+"))
        print('Destination IP Port:', port_num['dest'], file=open(filename, "a+"))

        rule_matched = False

        for rule in acl_rules:
            agreements = 0

            if rule[0] != 'Any':
                flag = True
                ip_addr_check = rule[0].split('.')
                for i in range(4):
                    if (ip_addr_check[i] != '*') and (ip_addr['src'][i] != int(ip_addr_check[i])):
                        flag = False
                        break
                if flag:
                    agreements = agreements + 1
            else:
                agreements = agreements + 1

            if rule[1] != 'Any':
                port_num_check = rule[1]
                if (port_num_check == port_num['src']):
                    agreements = agreements + 1
            else:
                agreements = agreements + 1

            if rule[2] != 'Any':
                flag = True
                ip_addr_check = rule[2].split('.')
                for i in range(4):
                    if (ip_addr_check[i] != '*') and (ip_addr['dest'][i] != int(ip_addr_check[i])):
                        flag = False
                        break
                if flag:
                    agreements = agreements + 1
            else:
                agreements = agreements + 1

            if rule[3] != 'Any':
                port_num_check = rule[3]
                if (port_num_check == port_num['dest']):
                    agreements = agreements + 1
            else:
                agreements = agreements + 1

            if (agreements == 4):
                print('Action:', rule[4], file=open(filename, "a+"))
                rule_matched = True

            if rule_matched == True:
                break

    # ARP Packet
    elif etherType[0] == 8 and etherType[1] == 6:

        print('Packet Type: ARP', file=open(filename, "a+"))

        ip_addr = dict()

        ip_addr['src'] = data[28:32]
        ip_addr['dest'] = data[38:42]

        port_num = dict()
        port_num['src'] = (data[34] << 8) + data[35]
        port_num['dest'] = (data[36] << 8) + data[37]

        print('Source IP Address:', ".".join(map(str, ip_addr['src'])), file=open(filename, "a+"))
        print('Destination IP Address:', ".".join(map(str, ip_addr['dest'])), file=open(filename, "a+"))

        print('Action: Deny', file=open(filename, "a+"))


def main():

    acl_rules = acl_rule_extractor()

    a = sniff(count=1, filter="host 10.100.53.3")
    dump_str = chexdump(a[0], dump=True)
    print(dump_str)
    hexdump_str = ' '.join(list(map(lambda x: x[-2:], dump_str.split(','))))
    hexdump_parser(hexdump_str, acl_rules, 'test.txt')

if __name__ == '__main__':
    main()
