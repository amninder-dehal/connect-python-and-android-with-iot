import paho.mqtt.client as paho
client= paho.Client()
client.connect("broker.mqttdashboard.com", 1883)
client.subscribe("second")
while True:
     client.publish('second',input(">> "))
     pass
