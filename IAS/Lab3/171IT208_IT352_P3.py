import pandas as pd
import math
import numpy as np
from scapy.all import *

class packet:

	def __init__(self):
		self.dump=None
		self.dest_mac = None
		self.src_mac = None
		self.frame_len = 0
		self.ipv = 0
		self.protocol = None
		self.src_ip = None
		self.dest_ip = None
		self.src_port = None
		self.dest_port = None

	def extract_fields(self,pkt_str):
		#f=open(dump_file_name, "r")

		#self.dump = f.read().split()
		self.dump = list(map(lambda x: int(x,16), pkt_str.split()))
		#print(self.dump)

		self.dest_mac = pkt_str.split()[0:6]
		self.src_mac = pkt_str.split()[6:12]
		self.frame_len = self.dump[12:14]

		if self.dump[23] == 6:
			self.protocol = 'TCP'
		elif self.dump[23] == 17:
			self.protocol = 'UDP'
		#print(self.dump[4])

		self.ipv = self.dump[14]>>4
		self.src_ip = self.dump[26:30]
		self.dest_ip = self.dump[30:34]

		self.src_port = (self.dump[34]<<8) + self.dump[35]
		self.dest_port = (self.dump[36] << 8) + self.dump[37]
		#print(self.dump[34])

	def Addr_maker(self,ip_list):

		addr = ""

		if len(ip_list) == 4:
			for i in range(4):
				addr = addr+str(ip_list[i])+"."

		elif len(ip_list) == 6:
			for i in range(6):
				addr = addr+str(ip_list[i])+":"

		return addr



	def print_fields(self):
		print("Packet Type = ",self.ipv)
		print("Packet Protocol = ",self.protocol)
		print("Source MAC Address = "+self.Addr_maker(self.src_mac)+"\nDestination MAC Address = "+self.Addr_maker(self.dest_mac))
		print("Source IP Address = "+self.Addr_maker(self.src_ip)+"\nDestination IP Address = "+self.Addr_maker(self.dest_ip))
		print("Source Port Number = "+str(self.src_port)+"\nDestination Port number = "+str(self.dest_port))

def extract_acl_rules(ACL_File_name):
	'''xl_file = pd.ExcelFile(file_name)
	dfs = {sheet_name: xl_file.parse(sheet_name) 
          for sheet_name in xl_file.sheet_names}'''
	df2 = pd.read_excel(ACL_File_name,na_values = []).fillna(-1)
	acl_rules = df2.values

	num_rules = 0
	num_cols = acl_rules.shape[1]

	for i in range(acl_rules.shape[0]):
		flag = 1
		for j in range(acl_rules.shape[1]):
			if acl_rules[i][j] == -1:
				flag = 0
				break

		if flag==0:
			break
		else:
			num_rules = num_rules+1

	acl_rules = acl_rules[:num_rules,:]

	#print(num_rules)
	return acl_rules

	#acl_rules.drop(acl_rules[:,0])
	#print(acl_rules)
def ipmatch(ip1,ip2):

	flag = 1

	if ip2=='Any':
		return True

	ip2 = ip2.split('.')

	#print(ip2)

	for i in range(len(ip1)):
		if ip2[i] == '*':
			continue
		if ip1[i] !=  int(ip2[i]):
			flag=0
			break

	return (flag!=0)

def portmatch(port1,port2):
	if port2=='Any':
		return True

	if port1==int(port2):
		return True

	return False


def firewall(pkt,acl_rules):

	for i in range(acl_rules.shape[0]):
		rule = acl_rules[i,:]
		if ipmatch(pkt.src_ip,rule[0]) and portmatch(pkt.src_port,rule[1]) and ipmatch(pkt.dest_ip,rule[2]) and portmatch(pkt.dest_port,rule[3]):
			print("\nAction for this packet as per the given ACL is : "+rule[4])
			return rule[4]
			break


def main():

	p = packet()

	acl_rules = extract_acl_rules("ACL-File-Lab-Program-3.xlsx")

	
	#print("Testcase ",(i+1))
	testcase_filter = input("Enter the filter for the sniffing : ")
		#filter="host 10.10.1.1"
	pkts = sniff(filter=testcase_filter,count = 1,timeout=10)
	pkt_dump = chexdump(pkts[0],dump=True)

	dump_string = ' '.join(list(map(lambda x: x[-2:], pkt_dump.split(','))))
	#print(dump_string)
	print("The packet fields are : ")
	p.extract_fields(dump_string)

	p.print_fields()

	action = firewall(p,acl_rules)
	if action == 'allow':
		print("The packet is allowed")
	else:
		print("The packet is denied")

	print("\n\n#################################################################\n\n")



	'''f=open("IT352_Lab2_Testcases.txt", "r")

	pkts = f.read().split('\n')

	print(len(pkts))

	actions = []

	j=1

	for i in range(len(pkts)):
		if len(pkts[i])>0:
			print("Details about packet "+str(j)+"\n")
			p = packet()
			p.extract_fields(pkts[i])
			p.print_fields()
			acl_rules = extract_acl_rules("ACL-File.xlsx")
			action = firewall(p,acl_rules)
			actions.append(action)
			j = j+1
			print("\n\n\n")

	print("The final actions for the packets as per ACL are : \n",actions)'''
			





if __name__=='__main__':
	main()