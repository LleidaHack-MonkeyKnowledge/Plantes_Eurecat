from paho.mqtt import client as mqtt

broker = '84.88.76.18'
port = 1883
topic = "hackeps/eurecat" #"hackeps/eurecat"
user = 'regimiento_agroguardia'
password = 'R3g1m3nt@gr0gu4rd14'
client_id = 'MonkeyKnowledge'

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

def on_message(client, userdata, msg):
    print("bieen")
    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

def connect_mqtt():
    # Set Connecting Client ID
    client = mqtt.Client(client_id)
    client.username_pw_set(user, password)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port)
    
    return client

def run():
    client = connect_mqtt()
    client.subscribe(topic)
    client.loop_forever()


#______________
#   MAIN
#______________

run()