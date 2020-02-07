# first of all import the socket library 
import socket
import random            

# next create a socket object 
s = socket.socket()      
print("Socket successfully created")

# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 12345 + random.randint(1,100)   #generating a port number such that it is free         

# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests 
# coming from other computers on the network 
hostname = socket.gethostname()
ip_addr_server = socket.gethostbyname(hostname)
s.bind(('', port))   
print("IP address of server = ",ip_addr_server)    
print("Socket bound to prt number : ",port) 

# put the socket into listening mode 
s.listen(5)  
print("socket is listening")            

# a forever loop until we interrupt it or 
# an error occurs 
for i in range(1): 

    flag=1

# Establish connection with client. 
    c,addr = s.accept()  
    print('Got connection from',addr) 

    client_id = c.recv(1024).decode('ascii').split()
    print("\n\nThe ID Of the client :\nHostname = ",client_id[0],"\nIP Address = ",client_id[1],"\n\n")

    for i in range(3):

        print("ROUND ",(i+1))

    # send a thank you message to the client. 
        #c.send('Thank you for connecting'.encode('utf-8')) 
        client_info = c.recv(1024).decode('ascii').split()
        x = int(client_info[0])
        v = int(client_info[1])
        n = int(client_info[2])

        print("Witness = ",x,"\nClient's Public key = ",v,"\nGlobal Parameter , n = ",n)

        challenge = int(input("Enter the challenge : "))

        c.send(str(challenge).encode('utf-8'))

        y = int(c.recv(1024).decode('ascii'))
        print("y = ",y)

        verifier1 = ((y%n)*(y%n))%n
        verifier2 = x%n

        if challenge==1:
            verifier2 = (verifier2*(v%n))%n # basically (x*y^1)mod n

        #print("verifier1 = ",verifier1,"\nverifier2 = ",verifier2)

        if verifier1==verifier2:
            print("\nRound cleared\n")


        else:
            print("\nRound NOT cleared")
            flag=0
            break

        print("\n******************************************************\n")

    if flag==0:
        print("\nClient NOT authenticated\n")
    else:
        print("\nClient is authenticated\n")

    # Close the connection with the client 
    c.close() 