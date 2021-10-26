import paho.mqtt.client as mqtt


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe("Test_IFN649")
    client.subscribe("soil_moisture")
    client.subscribe("air_temperature")
    client.subscribe("air_humidity")
    client.subscribe("pressure")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+' '+str(msg.payload))
    m_topic = msg.payload.decode('utf-8')
    result = m_topic.split(' ')
    # print(result)
    val = float(result[-2])
    # print(val)
    if msg.topic == 'soil_moisture':
        # float(str(msg.payload))
        if val < 67:
            print("\t soil not wet enough, need some water for irrigation")
        # elif float(row[2]) < 40:
        # 	print("suitable zone")
        elif val > 80:
            print('too wet, soil wet enough')

    if msg.topic == 'air_temperature':
        # float(str(msg.payload))
        if val < 15:
            print("\t so cold, need to open the heater")

        elif val > 28:
            print('so hot, need to open air-conditioner')

    if msg.topic == 'air_humidity':
        # float(str(msg.payload))
        if val < 60:
            print("\t too dry, need to open the air humidifier")

        elif val > 85:
            print('alert： need to reduce humidity')

    # print('-' * 50)


    # if msg.topic == 'temperature':
    #     if float(msg.payload) < 25:
    #         print("\t Low temperature, not suitable for plant")
    #         alert = 'low temperature'
    #     # elif float(row[2]) < 40:
    #     # 	print("suitable zone")
    #     elif float(msg.payload) > 35:
    #         print('too hot, reduce the temperature')
    #         alert = 'too hot'

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("174.129.60.239", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
