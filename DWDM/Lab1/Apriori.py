import itertools 
from itertools import combinations, chain 
import numpy as np
import pandas as pd

def findSubsets(s, n): 
    return list(map(set, itertools.combinations(s, n))) 

def aprioriForSmallDataset():
	pd1 = pd.read_csv('test_dataset.csv',header=None).fillna('')
	pd1 = pd1.values
	#print(pd1)

	all_transactions=[]
	for i in range(pd1.shape[0]):
		transaction=set()
		for j in range(pd1.shape[1]):
			if pd1[i][j]=='':
				break
			transaction.add(pd1[i][j])
		all_transactions.append(transaction)

	

	min_support = int(input("Enter the minimum support value : "))
	min_confidence = float(input("Enter the minimum confidence as fraction : "))

	C=[None]*10
	L=[None]*10
	assocRules=[None]*10
	#C_supports = [None]*10
	L_supports = [None]*10
	for i in range(10):
		C[i] = list()
		L[i] = list()
		assocRules[i] = list()
		#C_supports[i] = list()
		L_supports[i] = list()

	#C1 =[]
	unique_items = set()
	for i in range(len(all_transactions)):
		unique_items = unique_items.union(all_transactions[i])

	for item in unique_items:
		support_count=0
		for transaction in all_transactions:
			if item in transaction:
				support_count+=1
		if support_count>=min_support:
			L[0].append({item})
			L_supports[0].append(support_count)
		C[0].append({item})

	print("C1 = \n")
	for itemset in C[0]:
		print(itemset)
	#print(C[0])

	print("\n********************************************************\n")

	print("L1 = \n")
	for itemset in L[0]:
		print(itemset)
	print("\nThe respective Supports are :\n")
	for support_value in L_supports[0]:
		print(support_value)

	print("\n********************************************************\n")

	#L1 = []
	for k in range(1,10):

		sz = len(L[k-1])
		for i in range(sz):
			itemset1 = list(L[k-1][i])
			for j in range(i+1,sz):
				itemset2 = list(L[k-1][j])
				flag = 1
				for t in range(k-1):
					if itemset1[t]!=itemset2[t]:
						flag=0
						break
				if flag==1:
					C[k].append(L[k-1][i].union(L[k-1][j]))



		if len(C[k])==0:
			break

		for itemset in C[k]:
			support_count=0
			for t in all_transactions:
				if itemset.intersection(t)==itemset:
					support_count+=1
			if support_count>=min_support:
				L[k].append(itemset)
				L_supports[k].append(support_count)

		'''for itemset in L[k]:

			subsets = findSubsets(itemset,1)
			itemset_count=0

			for transaction in all_transactions:
				if transaction.intersection(itemset)==itemset:
					itemset_count += 1

			for subset in subsets:
				
				complementary = itemset.difference(subset)
				subset_count=0

				for transaction in all_transactions:
					if transaction.intersection(subset)==subset:
						subset_count += 1

				if (float)(itemset_count/subset_count)>min_confidence:
					assocRules[k].append(str(subset)+"=>"+str(complementary))

				complementary,subset = subset,complementary
				subset_count=0

				for transaction in all_transactions:
					if transaction.intersection(subset)==subset:
						subset_count += 1

				if (float)(itemset_count/subset_count)>min_confidence:
					assocRules[k].append(str(subset)+"=>"+str(complementary))'''

		for itemset in L[k]:

			itemset_count = 0
			for transaction in all_transactions:
				if transaction.intersection(itemset)==itemset:
					itemset_count += 1

			for n in range(1,(k+1)):
				subsets = findSubsets(itemset,n)

				for subset in subsets:
					complementary = itemset.difference(subset)
					subset_count=0

					for transaction in all_transactions:
						if transaction.intersection(subset)==subset:
							subset_count += 1

					conf  = (float)(itemset_count/subset_count)

					if conf >min_confidence:
						assocRules[k].append(str(subset)+"=>"+str(complementary)+"\t"+str(conf))

		if len(L[k])==0:
			break

		print("C",(k+1)," = \n")
		for itemset in C[k]:
			print(itemset)

		print("\n********************************************************\n")

		print("L",(k+1)," = \n")
		for itemset in L[k]:
			print(itemset)

		print("\n********************************************************\n")

		print("\nThe respective Supports are :\n")
		for support_value in L_supports[k]:
			print(support_value)

		print("\n********************************************************\n")

		print("\nThe Association rules for L",(k+1),"are :\n")
		for rule in assocRules[k]:
			print(rule)

		print("\n********************************************************\n")

def aprioriForLargeDataset():
	pd1 = pd.read_csv('retail_dataset.csv').fillna('')
	pd1 = pd1.values
	#print(pd1)

	all_transactions=[]
	for i in range(pd1.shape[0]):
		transaction=set()
		for j in range(pd1.shape[1]):
			if pd1[i][j]=='':
				break
			transaction.add(pd1[i][j])
		all_transactions.append(transaction)

	print(len(all_transactions))

	

	min_support = int(input("Enter the minimum support value : "))
	#min_confidence = float(input("Enter the minimum confidence as fraction"))

	C=[None]*100
	L=[None]*100
	#C_supports = [None]*10
	L_supports = [None]*10
	for i in range(10):
		C[i] = list()
		L[i] = list()
		#C_supports[i] = list()
		L_supports[i] = list()

	#C1 =[]
	unique_items = set()
	for i in range(len(all_transactions)):
		unique_items = unique_items.union(all_transactions[i])

	for item in unique_items:
		support_count=0
		for transaction in all_transactions:
			if item in transaction:
				support_count+=1
		if support_count>=min_support:
			L[0].append({item})
			L_supports[0].append(support_count)
		C[0].append({item})

	'''print("\n********************************************************\n")
	print("L1 = \n")
	for itemset in L[0]:
		print(itemset)
	print("\nThe respective Supports are :\n")
	for support_value in L_supports[0]:
		print(support_value)
	print("\n********************************************************\n")'''

	print("Length of C1 = ",len(C[0]))
	print("\n********************************************************\n")
	print("Length of L1 = ",len(L[0]))
	print("\n********************************************************\n")

	#L1 = []
	for k in range(1,10):

		sz = len(L[k-1])
		for i in range(sz):
			itemset1 = list(L[k-1][i])
			for j in range(i+1,sz):
				itemset2 = list(L[k-1][j])
				flag = 1
				for t in range(k-1):
					if itemset1[t]!=itemset2[t]:
						flag=0
						break
				if flag==1:
					C[k].append(L[k-1][i].union(L[k-1][j]))



		if len(C[k])==0:
			break

		for itemset in C[k]:
			support_count=0
			for t in all_transactions:
				if itemset.intersection(t)==itemset:
					support_count+=1
			if support_count>=min_support:
				L[k].append(itemset)
				L_supports[k].append(support_count)

		'''print("L",(k+1)," = \n")
		for itemset in L[k]:
			print(itemset)
		print("\n********************************************************\n")
		print("\nThe respective Supports are :\n")
		for support_value in L_supports[k]:
			print(support_value)
		print("\n********************************************************\n")'''

		print("Length of C",(k+1)," = ",len(C[k]))
		print("\n********************************************************\n")
		print("Length of L",(k+1)," = ",len(L[k]))
		print("\n********************************************************\n")

def main():
	aprioriForSmallDataset()
	#aprioriForLargeDataset()


if __name__ == '__main__':
	main()



