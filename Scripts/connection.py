from paho.mqtt import client as mqtt

broker = '84.88.76.18'
port = 1883
topic = "hackeps/RA" #"hackeps/eurecat"
user = 'regimiento_autoguardia'
password = 'R3g1m3nt@gr0gu4rd14'
client_id = 'MonkeyKnowledge'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client
