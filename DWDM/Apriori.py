import numpy as np
import pandas as pd


def main():
	pd1 = pd.read_csv('test_dataset_1.csv',header=None).fillna('')
	pd1 = pd1.values
	database=[]
	for i in range(pd1.shape[0]):
		transaction=set()
		for j in range(pd1.shape[1]):
			if pd1[i][j]=='':
				break
			transaction.add(pd1[i][j])
		database.append(transaction)

	print("The database is :")
	for transaction in database:
		print(transaction) 
	print()
	
	min_support = int(input("Enter the minimum support value : "))

	C=[None]*10
	L=[None]*10
	#C_supports = [None]*10
	L_supports = [None]*10
	for i in range(10):
		C[i] = list()
		L[i] = list()
		#C_supports[i] = list()
		L_supports[i] = list()

	for i in range(pd1.shape[0]):
		for j in range(pd1.shape[1]):
			if pd1[i][j]=='':
				break
			if {pd1[i][j]} not in C[0]:
				ele = {pd1[i][j]}
				C[0].append(ele)

	print("C1 = \n")
	for itemset in C[0]:
		print(itemset)

	print("\n********************************************************\n")

	#C1.remove('')

	#L1 = []
 

	'''for ele in C[0]:
		count = 0
		for i in range(pd1.shape[0]):
			for j in range(pd1.shape[1]):
				if pd1[i][j]=='':
					break
				if pd1[i][j]==ele:
					count = count+1
					break#since we are counting only the no of transactions
		if count>=min_support:
			L_supports[0].append(count)
			L[0].append(ele)'''

	print("L1 = \n")
	print("Member\t\tSupport")
	for i in range(len(L[0])):
		print(L[0][i],"\t\t",L_supports[0][i])

	print("\n********************************************************\n")

	#L1 = pd.DataFrame(L1) 

	#C2 = []
	'''k=1
	while len(C[k-1])>0 and len(L[k-1])>0:

		for i in range(len(L[k-1])):
			ele = [L[k-1][i]]
		#print(C2_ele)
			for j in range(i+1,len(L[k-1])):
				flag = 1
				for c in range(k-1):
					if L[k-1][j] 
				C2_member = C2_ele[:]
				C2_member.append(L[0][j])
				C[1].append(C2_member)

		print("C2 = \n")
		for itemset in C[1]:
			print(itemset)

		print("\n********************************************************\n")

	#L2 = []
		for itemset in C[1]:
			transactions_count = 0
			for i in range(pd1.shape[0]):
				items_found = 0
				for item in itemset:
					for j in range(pd1.shape[1]):
						if pd1[i][j]==item:
							items_found=items_found+1
							break
				if items_found == len(itemset):
					transactions_count = transactions_count+1
			if transactions_count>=min_support:
				L[1].append(itemset[:])
				L_supports[1].append(transactions_count)
			#print(transactions_count)
		print("L2 = \n")
		print("Member\t\tSupport")
		for i in range(len(L[1])):
			print(L[1][i],"\t\t",L_supports[1][i])

		print("\n********************************************************\n")

		k = k+1'''



if __name__ == '__main__':
	main()



'''import pandas as pd
import numpy as np

def activation(A):
	for i in range(A.shape[0]):
		if(A[i]>0):
			A[i]=1
		else:
			A[i]=0
	return A
def activation2(A):
	for i in range(A.shape[0]):
		if(A[i][0]>0):
			A[i][0]=1
		else:
			A[i][0]=0
	return A

def main():

	print("Using IRIS dataset")

	df1=pd.read_csv('IRIS.csv')
	#print(df1)
	df1["class"]=df1["class"].astype('category')
	df1["class_cat"]=df1["class"].cat.codes
	df1=df1.drop(columns=['class'])

	df1=df1.values#convert dataframe to numpy matrix
	np.random.shuffle(df1)
	X=df1[:,:-1]
	Y=df1[:,-1]
	I=np.ones((X.shape[0],1))
	X=np.concatenate((I,X),axis=1)
	m=X.shape[0]
	Y=Y.reshape((m,1))

	sz_test=(int)(m/10)
	sz_train=m-sz_test

	alpha=0.1
	while(alpha<=1.0):
		print("Using learning rate : ",alpha)
		precision=0
		recall=0
		accuracy=0
		for i in range(10):
			i1=(i*sz_test)
			i2=((i+1)*sz_test)
			X_test,X_train = X[i1:i2,:],np.concatenate((X[0:i1,:],X[i2:m,:]),axis=0)
			Y_test,Y_train = Y[(i*sz_test):((i+1)*sz_test),:],np.concatenate((Y[0:i1,:],Y[i2:m,:]),axis=0)
	#X_train.shape

			W=np.random.rand(X_train.shape[1],1)
		#threshold=0
			
			ex_no=0
			for i in range(500):
				prod=np.dot(X_train[ex_no,:],W)
				a=activation(np.dot(X_train[ex_no,:],W))
				J=Y_train[ex_no]-a[0]
				change=(alpha*J)*X_train[ex_no,:]
				change=change.reshape(X.shape[1],1)
			
				W=np.add(W,change)
				ex_no=(ex_no+1)%sz_train

			prod=np.dot(X_test,W)
		#print("Shape is ",prod.shape)

			a=activation2(prod)

			fp,fn,tp,tn=0,0,0,0
			for i in range(a.shape[0]):
			#print(a[i]," ",Y_test[i],"\n")
				if(a[i][0]==0 and Y_test[i]==0):
					tn+=1
				elif(a[i][0]==0 and Y_test[i]==1):
					fn+=1
				elif(a[i][0]==1 and Y_test[i]==0):
					fp+=1
				elif(a[i][0]==1 and Y_test[i]==1):
					tp+=1

			print("FP, TP, FN, TN ",fp,tp,fn,tn)

			precision+=tp/(tp+fp)
			recall+=tp/(tp+fn)
			accuracy+=(tp+tn)/(tp+tn+fp+fn)

		precision=(float)(precision/10)
		recall=(float)(recall/10)
		accuracy=(float)(accuracy/10)
		print("Accuracy, Precision and Recall : ",accuracy," ",precision," ",recall,"\n\n")
		alpha+=0.1

	print("\n\nUsing SPECT dataset\n\n")

	df2=pd.read_csv('SPECT.csv')
	#print(df1)
	df2["Class"]=df2["Class"].astype('category')
	df2["class_cat"]=df2["Class"].cat.codes
	df2=df2.drop(columns=['Class'])

	df2=df2.values#convert dataframe to numpy matrix
	np.random.shuffle(df2)
	X=df2[:,:-1]
	Y=df2[:,-1]
	I=np.ones((X.shape[0],1))
	X=np.concatenate((I,X),axis=1)
	m=X.shape[0]
	Y=Y.reshape((m,1))

	sz_test=(int)(m/10)
	sz_train=m-sz_test

	alpha=0.1
	while(alpha<=1.0):
		print("Using learning rate : ",alpha)
		precision=0
		recall=0
		accuracy=0
		for i in range(10):
			i1=(i*sz_test)
			i2=((i+1)*sz_test)
			X_test,X_train = X[i1:i2,:],np.concatenate((X[0:i1,:],X[i2:m,:]),axis=0)
			Y_test,Y_train = Y[(i*sz_test):((i+1)*sz_test),:],np.concatenate((Y[0:i1,:],Y[i2:m,:]),axis=0)
	#X_train.shape

			W=np.random.rand(X_train.shape[1],1)
		#threshold=0
			
			ex_no=0
			for i in range(500):
				prod=np.dot(X_train[ex_no,:],W)
				a=activation(np.dot(X_train[ex_no,:],W))
				J=Y_train[ex_no]-a[0]
				change=(alpha*J)*X_train[ex_no,:]
				change=change.reshape(X.shape[1],1)
			
				W=np.add(W,change)
				ex_no=(ex_no+1)%sz_train

			prod=np.dot(X_test,W)
		#print("Shape is ",prod.shape)

			a=activation2(prod)

			fp,fn,tp,tn=0,0,0,0
			for i in range(a.shape[0]):
			#print(a[i]," ",Y_test[i],"\n")
				if(a[i][0]==0 and Y_test[i]==0):
					tn+=1
				elif(a[i][0]==0 and Y_test[i]==1):
					fn+=1
				elif(a[i][0]==1 and Y_test[i]==0):
					fp+=1
				elif(a[i][0]==1 and Y_test[i]==1):
					tp+=1

			print("FP, TP, FN, TN ",fp,tp,fn,tn)

			precision+=tp/(tp+fp)
			recall+=tp/(tp+fn)
			accuracy+=(tp+tn)/(tp+tn+fp+fn)

		precision=(float)(precision/10)
		recall=(float)(recall/10)
		accuracy=(float)(accuracy/10)
		print("Accuracy, Precision and Recall : ",accuracy," ",precision," ",recall,"\n\n")
		alpha+=0.1

	print("\n\nUsing SPECTF dataset\n\n")

	df3=pd.read_csv('SPECTF.csv')
	#print(df1)
	df3["Class"]=df3["Class"].astype('category')
	df3["class_cat"]=df3["Class"].cat.codes
	df3=df3.drop(columns=['Class'])

	df3=df3.values#convert dataframe to numpy matrix
	np.random.shuffle(df3)
	X=df3[:,:-1]
	Y=df3[:,-1]
	I=np.ones((X.shape[0],1))
	X=np.concatenate((I,X),axis=1)
	m=X.shape[0]
	Y=Y.reshape((m,1))

	sz_test=(int)(m/10)
	sz_train=m-sz_test

	alpha=0.1
	while(alpha<=1.0):
		print("Using learning rate : ",alpha)
		precision=0
		recall=0
		accuracy=0
		for i in range(10):
			i1=(i*sz_test)
			i2=((i+1)*sz_test)
			X_test,X_train = X[i1:i2,:],np.concatenate((X[0:i1,:],X[i2:m,:]),axis=0)
			Y_test,Y_train = Y[(i*sz_test):((i+1)*sz_test),:],np.concatenate((Y[0:i1,:],Y[i2:m,:]),axis=0)
	#X_train.shape

			W=np.random.rand(X_train.shape[1],1)
		#threshold=0
			
			ex_no=0
			for i in range(500):
				prod=np.dot(X_train[ex_no,:],W)
				a=activation(np.dot(X_train[ex_no,:],W))
				J=Y_train[ex_no]-a[0]
				change=(alpha*J)*X_train[ex_no,:]
				change=change.reshape(X.shape[1],1)
			
				W=np.add(W,change)
				ex_no=(ex_no+1)%sz_train

			prod=np.dot(X_test,W)
		#print("Shape is ",prod.shape)

			a=activation2(prod)

			fp,fn,tp,tn=0,0,0,0
			for i in range(a.shape[0]):
			#print(a[i]," ",Y_test[i],"\n")
				if(a[i][0]==0 and Y_test[i]==0):
					tn+=1
				elif(a[i][0]==0 and Y_test[i]==1):
					fn+=1
				elif(a[i][0]==1 and Y_test[i]==0):
					fp+=1
				elif(a[i][0]==1 and Y_test[i]==1):
					tp+=1

			print("FP, TP, FN, TN ",fp,tp,fn,tn)

			precision+=tp/(tp+fp)
			recall+=tp/(tp+fn)
			accuracy+=(tp+tn)/(tp+tn+fp+fn)

		precision=(float)(precision/10)
		recall=(float)(recall/10)
		accuracy=(float)(accuracy/10)
		print("Accuracy, Precision and Recall : ",accuracy," ",precision," ",recall,"\n\n")
		alpha+=0.1


if __name__=='__main__':
	main()
'''