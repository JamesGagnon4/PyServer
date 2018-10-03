__author__ = 'James Gagnon'
import socket
import http.server
PORT = 8000
HOST = ''
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind((HOST, PORT))
serverSocket.listen(1)
print('Server is operating on port ', PORT, '\n')
print('Enter QUIT to exit.')
# prepare server connection

while True:

        client_connection, client_address = serverSocket.accept()
        request = client_connection.recv(1024).decode()
        print(request)

        filename = request.split()[1]               # determine filename
        print (filename)                              # DEBUG: to check filename

        try:
             f = open(filename[1:])                      # open the file
             outputdata = f.read()                       # outputdata = data in the file requested
             print (outputdata)
             client_connection.send(outputdata.encode())
             client_connection.close()

        except IOError:
             print("Error code 404: File not found.")
             client_connection.send(("Error code 404: File not found \n").encode())

             client_connection.send(("Please try another file").encode())
             client_connection.close()


