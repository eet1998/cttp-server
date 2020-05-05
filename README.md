# Calc Text Transfer Protocol (CTTP) Server
A server for a fictitious Calc Text Transfer Protocol (CTTP).

## Summary
The job of this server is to send an announcement any time a client connects to inform about the supported operations. Then, the server listens for requests and returns appropriate responses back to the client until the client terminates the connection.

## Client-Server Interaction
When a CTTP Client connects to the listening port of a CTTP server, the server immediately sends usage instructions listing the available capabilities. It then listens for requests from the client. Upon receipt of the usage instructions, a client may send requests to the server. Upon receipt of a request, a server responds to the client with an appropriate response.

## How to Run This Code
1. Fire up your local terminal and type `git clone https://github.com/eet1998/cttp-server.git`. 
2. Type `python3 cttpserver.py 12345`.
3. In a second terminal window, type `python3 cttpclient.py localhost 12345 testinput.txt`. Feel free to modify `testinput.txt` to change up the requests from the client.
