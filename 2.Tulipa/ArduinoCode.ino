#include <PubSubClient.h>
#include <ESP8266WiFi.h>
#include <DHT.h>

const char* ssid = "iPhone";
const char* password = "oogabuga";
const char* broker = "84.88.76.18";
const int port = 1883;
const char* topic = "hackeps/RA";
const char* user = "regimiento_agroguardia";
const char* password_mqtt = "R3g1m3nt@gr0gu4rd14";
const char* clientID = "MonkeyKnowledge";
DHT dht(D5,DHT11);

WiFiClient espClient;
PubSubClient client(espClient);

void setup_wifi() {
  delay(10);
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message received: ");
  Serial.println(topic);

  Serial.print("Payload: ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    if (client.connect(clientID, user, password_mqtt)) {
      Serial.println("connected");
      client.subscribe(topic);
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  dht.begin();
  setup_wifi();
  client.setServer(broker, port);
  //client.setCallback(callback);
  //client.loop();

  //Init Pins
  pinMode(D0, OUTPUT);  //Soil humidity sensor
  pinMode(D1, OUTPUT);  //Light sensor
  pinMode(D2, OUTPUT);  //Water pump
  pinMode(D5, INPUT);   //Air humidity & temperature sensor
  digitalWrite(D0, LOW);
  digitalWrite(D1, LOW);
  digitalWrite(D2, LOW);
}

void loop() {
  //Check connection
  if (!client.connected()) {
    reconnect();
  }

  //TEMPERATURE
  float temp = dht.readTemperature();
  int airHumid = dht.readHumidity(); 

  //ACTIVATE SOIL SENSOR
  digitalWrite(D1, HIGH);
  digitalWrite(D0, LOW);
  int humidityValue = analogRead(A0);
  humidityValue = 100 - (float(humidityValue) / 1024.0f * 100);
  delay(500);

  //ACTIVATE LIGHT SENSOR
  digitalWrite(D1, LOW);
  digitalWrite(D0, HIGH);
  int lightValue = analogRead(A0);

  //Water plant for 3 sec
  if(humidityValue > 50)
  { 
    digitalWrite(D2, HIGH);
    delay(3000);
    digitalWrite(D2, LOW);
  }

  //Generate JSON message with Data
  char msg[255];
  sprintf(msg, "{\"id\": \"Monkey Plant\", \"light\": %d, \"soil_humidity\": %d, \"air_humidity\": %d, \"temperature\": %.1f}", 
          lightValue, humidityValue, airHumid, temp);

  //Debug
  Serial.println(msg);
  
  //Send Message to BROKER
  if (!client.publish(topic, msg)) {
    Serial.println("Failed to send message");
  }
}