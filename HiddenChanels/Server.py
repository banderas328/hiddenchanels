import socket
import threading
import time

message_time = 0
start = 0
finish = 0
bind_ip = '127.0.0.1'
bind_port = 9999
hidden_message = ""
legal_message = ""
first_sumbol = True



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    if(bits):
        n = int(bits, 2)
        return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def is_timer_ok():
    print("timer")
    global message_time
    global hidden_message
    global legal_message
    global first_sumbol
    elapsed = time.time() - message_time
    elapsed = int(elapsed)
    print("STOPTIME=", elapsed)
    if elapsed < 10 :
        t = threading.Timer(6, is_timer_ok)
        t.start()
    else:
        if elapsed < 50:
            print("timer stoping decoding message")
            print(legal_message)
            print(hidden_message)
            hidden_message = hidden_message[2:]
            hidden_message = text_from_bits(hidden_message)
            print(hidden_message)
            server_restart()


def handle_client_connection(client_socket):
    global finish
    global start
    finish = time.time()
    global legal_message
    global hidden_message
    global message_time
    finish = time.time()
    message_time = int(round(time.time()))
    request = client_socket.recv(1024)
    delay = finish - start
    delay = int(delay)
    print ("DELAY=",delay)
    global first_sumbol
    if first_sumbol:
        first_sumbol = False
    elif delay == 0 :
        hidden_message += "0"
    else :
        hidden_message += "1"
    valid_letter =request.decode("utf-8")
    legal_message += valid_letter
    client_socket.close()
    start = time.time()

def server_restart():
    print("server restarting")
    global  message_time, start, finish ,bind_ip, bind_port, hidden_message, legal_message, first_sumbol
    message_time = time.time()
    start = 0
    finish = 0
    bind_ip = '127.0.0.1'
    bind_port = 9999
    hidden_message = ""
    legal_message = ""
    first_sumbol = True

    print ('Listening on {}:{}'.format(bind_ip, bind_port))
    print("start_timer")
    t = threading.Timer(6, is_timer_ok)
    t.start()

    while True:
        client_sock, address = server.accept()
        # print ('Accepted connection from {}:{}'.format(address[0], address[1]))
        client_handler = threading.Thread(
            target=handle_client_connection,
            args=(client_sock,)
        )
        client_handler.start()

server_restart()




