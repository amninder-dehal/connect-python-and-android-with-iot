import paho.mqtt.client as paho

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client, userdata, message):
    msfg= str(message.payload.decode('utf-8'))
    print(msfg)

client = paho.Client()
client.connect("broker.mqttdashboard.com", 1883)
client.subscribe("second")
print('')
client.on_subscribe = on_subscribe
client.on_message= on_message

client.loop_forever()
