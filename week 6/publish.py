import paho.mqtt.publish as publish
publish.single("Test", "Iris", hostname="localhost")
publish.single("Test2", "colin", hostname="localhost")
print("Done")
