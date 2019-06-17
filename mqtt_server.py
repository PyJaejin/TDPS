import paho.mqtt.client as mqtt
from requests import post
from pushbullet import send_warning_msg

send_url = "http://localhost:"
send_port = 9080
client = mqtt.Client()
client.connect("10.42.0.1", 1883, 60)

def on_connect(client, userdata, flags, rc):
    print("Connect!")
    client.subscribe("nRF52840_resources/temp_humi")

def on_message(client, userdata, msg):
    try:
        recv_msg = str(msg.payload)
        recv_msg = recv_msg.split(',')
        send_data = {
            'node_id': recv_msg[0],
            'temp_value': recv_msg[1],
            'humi_value': recv_msg[2][:recv_msg[2].find('.')+2]
        }
        if(float(send_data['temp_value']) >= 25):
            client.publish("nRF52840_resources/led3", '\x01')
            send_warning_msg(send_data['node_id'], send_data['temp_value'], send_data['humi_value'])
        else:
            client.publish("nRF52840_resources/led3", '\x00')
        print(send_data)
        post(send_url + str(send_port) + "/value", json=send_data)
    
    except Exception as e:
        print(e)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
