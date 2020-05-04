# References: https://www.geeksforgeeks.org/python-string-split/, https://www.programiz.com/python-programming/methods/list/remove, https://www.geeksforgeeks.org/python-check-for-float-string/ 

import socket
import sys
import math

class CalcTextServer(object):
    def __init__(self, host='', port=12345):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn = None
        self.addr = None
        self.transcript = []

    def run_server(self, terminate_on_close=False):
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)

        stay_alive = True
        while stay_alive:
            # accept a new connection
            self.conn, self.addr = self.socket.accept()
            # Send the Announcement
            ## TODO send the correct Announcement according to CTTP
            self.conn.sendall(b"Usage Instructions: ADD SUB MUL DIV ABS SQRT")
            
            # Accept a Request until this condition is set to False
            accept_query = True
            while accept_query:
                # Receive and decode some data
                request = self.conn.recv(1024).decode('utf-8')
                if not request: # ignore empty requests
                    break
                if "ADD" in request:
                    result = self.add(request)
                    if result == "long":
                        self.conn.sendall(b"CTTP/1.0 ERROR\nToo many arguments.")
                    elif result == "error":
                        self.conn.sendall(b"CTTP/1.0 ERROR\nArgument must be an integer or a float.")
                    else:
                        self.conn.sendall(b"CTTP/1.0 CALC\n%f\n" %result)
                if "SUB" in request:
                    result = self.sub(request)
                    if result == "long":
                        self.conn.sendall(b"CTTP/1.0 ERROR\nToo many arguments.")
                    elif result == "error":
                        self.conn.sendall(b"CTTP/1.0 ERROR\nArgument must be an integer or a float.")
                    else:
                        self.conn.sendall(b"CTTP/1.0 CALC\n%f\n" %result)
                if "MUL" in request:
                    result = self.mul(request)
                    if result == "long":
                        self.conn.sendall(b"CTTP/1.0 ERROR\nToo many arguments.")
                    elif result == "error":
                        self.conn.sendall(b"CTTP/1.0 ERROR\nArgument must be an integer or a float.")
                    else:
                        self.conn.sendall(b"CTTP/1.0 CALC\n%f\n" %result)
                if "DIV" in request:
                    result = self.div(request)
                    if result == "long":
                        self.conn.sendall(b"CTTP/1.0 ERROR\nToo many arguments.")
                    elif result == "error":
                        self.conn.sendall(b"CTTP/1.0 ERROR\nArgument must be an integer or a float.")
                    elif result == "zero":
                        self.conn.sendall(b"CTTP/1.0 ERROR\nSecond argument cannot be zero.")
                    else:
                        self.conn.sendall(b"CTTP/1.0 CALC\n%f\n" %result)
                if "ABS" in request:
                    result = self.abs(request)
                    if result == "long":
                        self.conn.sendall(b"CTTP/1.0 ERROR\nToo many arguments.")
                    elif result == "error":
                        self.conn.sendall(b"CTTP/1.0 ERROR\nArgument must be an integer or a float.")
                    else:
                        self.conn.sendall(b"CTTP/1.0 CALC\n%f\n" %result)
                if "SQRT" in request:
                    result = self.sqrt(request)
                    if result == "long":
                        self.conn.sendall(b"CTTP/1.0 ERROR\nToo many arguments.")
                    elif result == "error":
                        self.conn.sendall(b"CTTP/1.0 ERROR\nArgument must be an integer or a float.")
                    elif result == "neg":
                        self.conn.sendall(b"CTTP/1.0 ERROR\nArgument cannot be negative.")
                    else:
                        self.conn.sendall(b"CTTP/1.0 CALC\n%f\n" %result)
                elif "HELP" in request:
                    self.conn.sendall(b"CTTP/1.0 HELP\nADD SUB MUL DIV ABS SQRT")
                elif "BYE" in request:
                    self.conn.sendall(b"CTTP/1.0 BYE\nIt was nice calc'ing to you!\nCTTP/1.0 KTHXBYE\n")
                    stay_alive = False if terminate_on_close else True
                    accept_query = False # jump out of accept_query loop
                #elif not "ADD" or "SUB" or "MUL" or "DIV" or "ABS" or "SQRT" or "HELP" or "BYE" in request:
                    #self.conn.sendall(b"CTTP/1.0 ERROR\nUnkown request.")
            # This client is done, close the connection
            self.conn.close()
        # close socket at the end
        self.socket.close()

    def add(self, request):
        a_list = request.split()
        
        if len(a_list) > 5:
            return "long"

        try:
            var_1 = float(a_list[3])
            var_2 = float(a_list[4])
        except ValueError:
            return "error"

        result = var_1 + var_2
        return result

    def sub(self, request):
        a_list = request.split()
        
        if len(a_list) > 5:
            return "long"

        try:
            var_1 = float(a_list[3])
            var_2 = float(a_list[4])
        except ValueError:
            return "error"

        result = var_1 - var_2
        return result

    def mul(self, request):
        a_list = request.split()
        
        if len(a_list) > 5:
            return "long"

        try:
            var_1 = float(a_list[3])
            var_2 = float(a_list[4])
        except ValueError:
            return "error"

        result = var_1 * var_2
        return result

    def div(self, request):
        a_list = request.split()
        
        if len(a_list) > 5:
            return "long"

        try:
            var_1 = float(a_list[3])
            var_2 = float(a_list[4])
        except ValueError:
            return "error"

        if var_2 == 0:
            return "zero"

        result = var_1 / var_2
        return result
    
    def abs(self, request):
        a_list = request.split()
        
        if len(a_list) > 4:
            return "long"

        try:
            var = float(a_list[3])
        except ValueError:
            return "error"

        result = abs(var)
        return result

    def sqrt(self, request):
        a_list = request.split()
        
        if len(a_list) > 4:
            return "long"

        try:
            var = float(a_list[3])
        except ValueError:
            return "error"

        if var < 0:
            return "neg"

        result = math.sqrt(var)
        return result


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 24680
    c = CalcTextServer('', port)
    c.run_server(terminate_on_close=True)
