from paho.mqtt import client as mqtt
import saveToCsv as save

broker = '84.88.76.18'
port = 1883
topic = "hackeps/eurecat" #"hackeps/eurecat"
user = 'regimiento_agroguardia'
password = 'R3g1m3nt@gr0gu4rd14'
client_id = 'MonkeyKnowledge'

# Connection check
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

# When messages are recieved
def on_message(client, userdata, msg):
    print(msg.payload.decode())
    save.MessageToCsv(msg.payload.decode())

def connect_mqtt():
    # Client Setup
    client = mqtt.Client(client_id)
    client.username_pw_set(user, password)
    client.on_connect = on_connect
    client.on_message = on_message

    # Connect to broker
    client.connect(broker, port)
    
    return client

def run():
    # Client Setup
    client = connect_mqtt()

    # Listen Messages
    client.subscribe(topic)

    # Continuous Listening
    client.loop_forever()