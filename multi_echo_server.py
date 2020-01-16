from multiprocessing import Process

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s. setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(2)
        while True:
            conn, addr = s.accept()
            p = Process(targe= handle_request,args = (conn, addr, proxy_end))
            p.daemon = True
            p.start()
            print('started process', p)
def handle_echo(addr,conn):
    print( "Connected by", addr)
    full_data = conn.recv(BUFFER_SIZE)
    time.sleep(0.5)
    conn.sendall(full_data)
    conn.close()

if __name__ == '__main__':
    main()
