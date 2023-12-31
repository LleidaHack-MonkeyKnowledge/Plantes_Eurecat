import time

from paho.mqtt import client as mqtt

broker = '84.88.76.18'
port = 1883
topic = "hackeps/RA" #"hackeps/eurecat"
user = 'regimiento_agroguardia'
password = 'R3g1m3nt@gr0gu4rd14'
client_id = 'MonkeyKnowledge'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt.Client(client_id)
    client.username_pw_set(user, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client):
    msg_count = 1
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count = msg_count + 1
        if msg_count > 5:
            break

def run():
    client = connect_mqtt()
    #client.loop_start()
    publish(client)
    #client.loop_stop()

run()