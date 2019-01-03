import socket
from time import sleep

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9999))

legal_message = "hi to all this is legal message and everyone can see it hi to all this is legal message and everyone can see it hi to all this is legal message and everyone can see it hi to all this is legal message and everyone can see it hi to all this is legal message and everyone can see it"
hidden_message = "hacker"
binnary_message = text_to_bits(hidden_message)

binnary_message = "0" + binnary_message + "0"
print(binnary_message)
counter = 0
for i in binnary_message:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9999))
    print(counter)
    client.send(legal_message[counter].encode())
    print("itoe",i)

    if i != " ":
        print("int(i)",int(i)*3)
        sleep(int(i)*3)
    counter += 1









