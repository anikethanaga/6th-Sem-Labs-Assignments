# Import socket module 
import socket            

def main():

    # Define the port on which you want to connect 
    port = int(input("Enter port number of server to connect with : "))
    ip_addr_server = input("Enter IP address of server to connect with : ")

    # Create a socket object 
    sock = socket.socket()     


    hostname = socket.gethostname()    
    IPAddr = socket.gethostbyname(hostname)

    identity = hostname+" "+IPAddr

    # connect to the server on local computer 
    sock.connect((ip_addr_server, port))

    sock.send(identity.encode('utf-8'))

    print("Sending identity to server")

    for i in range(3):
    
        print("ROUND ",(i+1),"\n")

        p=int(input("Enter first prime number, p : "))
        q=int(input("Enter second prime number, q : ")) 
        n=p*q
        while True:
            s=int(input("Enter private key, s (a number between 1 and n-1) : "))
            if s<1 or s>=n:
                print("Out of range.Please enter again")
                continue
            break
        while True:
            r=int(input("Enter commitment, r (a random number between 1 and n-1) : "))
            if r<1 or r>=n:
                print("Out of range.Please enter again")
                continue
            break

        x = ((r%n)*(r%n))%n
        v = ((s%n)*(s%n))%n       

        parameters = str(x)+" "+str(v)+" "+str(n) 

        print("Sending public key and n to  server")          

        # receive data from the server 
        sock.send(parameters.encode('utf-8'))

        print("\nWaiting for challenge")

        challenge = int(sock.recv(1024).decode('ascii'))

        #print("Challenge = ",challenge)

        y = r%n
        if challenge==1:
            y = (y*(s%n))%n #basically y = (r*s^1)mod n

        print("\nSending response")

        sock.send(str(y).encode('utf-8'))

        print("\n******************************************************\n")

        # close the connection 
    sock.close()

if __name__=='__main__':
    main()