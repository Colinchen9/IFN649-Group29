import paho.mqtt.client as mqtt
import time
from abc import abstractmethod
#from threading import Thread

class ITopic
    def getTopic(self):
        return self.mName
        
    @abstractmethod
    def proc(self, msg):
        pass

class TemperatureTopic(ITopic):
    def __init__(self):
        self.mName = 'Temperature'

    def proc(self, msg):
        print(self.mName, ' : ', msg.payload.decode("utf-8"), "\n")
        # TODO: process messages for the topic of Temperature



class HumidityTopic(ITopic):
    def __init__(self):
        self.mName = 'Humidity'
    
    def proc(self, msg):
        print(self.mName, ' : ', msg.payload.decode("utf-8"), "\n")
        # TODO: process messages for the topic of Humidity


def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT.")
    print("Connection returned result: " + str(rc))

class MQTTClient:
    def __init__(self, addr, topic, clientNum):
        self.mClient = mqtt.Client(userdata=self)
        self.mClient.on_connect = self.on_connect
        self.mClient.on_message = self.on_message
        self.mClient.connect(addr, 1883, 60)
        self.mTopic = topic
        time.sleep(1)

    @staticmethod
    def on_connect(client, userdata, flags, rc):                
        #print("Thread" + str(userdata.mClientNum) + "(" +userdata.mTopic.mName + "): Connected to MQTT.")
        print("Connection returned result: " + str(rc) + "\n")
        
        userdata.mClient.subscribe(userdata.mTopic.mName)

    @staticmethod
    def on_message(client, userdata, msg):                     
        #print("Thread" + str(userdata.mClientNum) + ".")        
        userdata.mTopic.proc(msg)

    def start(self):
        self.mClient.loop_start()
            
    def stop(self):
        self.mClient.loop_stop(True)

def main():
    host = "localhost"
    
    client1 = MQTTClient(host, TemperatureTopic(), 1)
    #thread1 = Thread(target=client1.start())
    
    client2 = MQTTClient(host, HumidityTopic(), 2)
    #thread2 = Thread(target=client2.start())

    #client3 = MQTTClient("host", WeatherTopic(), 3)
    #thread3 = Thread(target=client3.start())

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        client1.stop()
        client2.stop()
        #client3.stop()
        pass

if __name__ == "__main__":
    main()
