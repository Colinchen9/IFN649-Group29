import paho.mqtt.client as mqtt


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("Test_IFN649")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    if msg.topic == 'tempereture':
        if float(msg.payload)) < 30:
            print("\t too dry, need some water")
            alert = 'too dry, need some water'
        # elif float(row[2]) < 40:
        # 	print("suitable zone")
        elif float(msg.payload)) > 40:
            print('too wet')
            alert = 'too wet'

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("52.91.101.106", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
