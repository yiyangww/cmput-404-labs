import socket, time, sys

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def get_remote_ip(host):
    print("Getting IP for {host}")
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("Hostname could not be resolved. Exiting")
        sys.exit()

    print("Ip address of {0} is {1}".format(host, remote_ip))
    return remote_ip

def main():

    host = "www.google.ca"
    port = 80
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
        print("Starting proxy server")
        proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # for the local host
        proxy_start.bind((HOST, PORT))
        proxy_start.listen(1)
        while True:
            conn, addr = proxy_start.accept()
            print("Connected by ", addr)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                print("Connecting to Google")
                remote_ip = get_remote_ip(host)

                proxy_end.connect((remote_ip, port))
                #proxy_end.connect((host, port))

                send_full_data = conn.recv(BUFFER_SIZE)
                print("Sending recieved data{0} to google".format(send_full_data))
                proxy_end.sendall(send_full_data)
                proxy_end.shutdown(socket.SHUT_WR)

                data = proxy_end.recv(BUFFER_SIZE)
                # after receive the data from the google server, send data to proxy clinet
                print("Sending recieved data{0} to client".format(data))
                conn.send(data)

            conn.close()

if __name__ == "__main__":
    main()
