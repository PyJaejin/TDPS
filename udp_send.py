import socket
from requests import post
from pushbullet import send_warning_msg

UDP_IP = "::"
UDP_PORT = 1234
send_url = "http://localhost:"
send_port = 9080

sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print("Hello")
    try:
        node_id, value = data.split(',')
        send_warning_msg(node_id, value)
        print("Sending..")
        send_data = {
            "node_id": str(node_id),
            "value": str(value)
        }
        post(send_url + str(send_port) + "/value", json=send_data)
        print("recv : "  + node_id, "recv2: " + value)
    except Exception as e:
        print(e) 
        continue
