import numpy as np 
import pandas as pd
from collections import defaultdict

class Node:
    
    def __init__(self, item_name, item_count):
        self.item = [item_name, item_count]
        self.children = defaultdict(lambda: None)

class FP_Tree:

    def __init__(self):
        self.root = Node(None,None)

    def insert(self,node,transaction):

        if transaction == []:
            return

        item = transaction[0]
        node_ = node.children[item]

        if node_ != None:
            node_.item[1] += 1
        else:
            node_ = Node(item, 1)
            node.children[item] = node_
        
        self.insert(node_, transaction[1:])


def main():
    dataset = pd.read_csv('test_dataset_1.csv', header=None)
    ds_entries = dataset.values

    freq_1_itemset = dict()

    for ds_entry in ds_entries:
        for value in ds_entry:
            if value in freq_1_itemset.keys(): 
                freq_1_itemset[value] += 1
            else:
                freq_1_itemset[value] = 1

    freq_1_itemset.pop(np.nan, None)

    transactions = []

    tree = FP_Tree()


    for ds_entry in ds_entries:
        transaction = [item for item in ds_entry if not (pd.isnull(item))]
        transaction.sort(key=lambda x: freq_1_itemset[x],reverse=True)
        transactions.append(transaction)
        tree.insert(tree.root,transaction)

    print(transactions)

    # tree.insert(tree.root, transactions[0])

    

if __name__ == '__main__':
    main()
