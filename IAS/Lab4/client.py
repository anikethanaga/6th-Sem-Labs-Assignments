# Import socket module 
import socket            

def main():
	p=int(input("Enter first prime number"))
	q=int(input("Enter second prime number")) 
	n=p*q
	while True:
		s=int(input("Enter s (a number between 1 and n-1)"))
		if s<1 or s>=n:
			print("Out of range.Please enter again")
				continue
		break
	while True:
		r=int(input("Enter r (a random number between 1 and n-1)"))
		if r<1 or r>=n:
			print("Out of range.Please enter again")
			continue
		break

	x = ((r%n)*(r%n))%n
	v = ((s%n)*(s%n))%n

	witness = str(x)+" "+str(v)+" "+str(n)


	# Create a socket object 
	s = socket.socket()      

	# Define the port on which you want to connect 
	port = int(input("Enter port number : "))                

	# connect to the server on local computer 
	s.connect(('127.0.0.1', port))



	# receive data from the server 
	print(s.recv(1024)) 
	# close the connection 
	s.close()    
