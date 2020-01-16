

import socket, sys

def create_tcp_socket():
    print('Creating socket')
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except (socket.error,msg):
        print('Failed to create socket. Error code:,')
        sys.exit()
    print("Socket created successfully")
    return s

def get_remote_ip(host):
    # connect to server
    try:
        remote_ip = socket.gethostbyname( host )
    except socket.gaierror:
        print( 'Hostname could not be resolved. Exiting')
        sys.exit()
    return remote_ip

def send_data(serversocket,payload):
    # send data to server
    print("Sending payload")
    try:
        serversocket.sendall(payload.encode())
    except socket.error:
        print( 'Send failed')
        sys.exit()
    print('Payload send successfully')


def main():
  try:
    host = 'www.google.com'
    port = 80
    payload = 'GET / HTTP/1.0\r\nHost: ' +host+'\r\n\r\n'
    buffer_size = 4096

    s =  create_tcp_socket()
    remote_ip = get_remote_ip(host)

    s.connect((remote_ip, port))

    print ('Socket connect to ' +host+ "on ip "+ remote_ip)

    send_data(s, payload)
    s.shutdown(socket.SHUT_WR)

    full_data = b""
    while True:
        data = s.recv(buffer_size)
        if not data:
            break
        full_data += data
    print(full_data)
  except Exception as e:
    print(e)
  finally:
    s.close()
if __name__ == '__main__':
    main()
