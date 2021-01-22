import paho.mqtt.client as mqtt


def run():
    print("method is calling")
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set("rohit", "rohit@123")
    client.connect("localhost", 1883)
    client.loop_forever()


def on_connect(client, userdata, flags, rc):
    print("connecting...")
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("test")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.payload))
    print(msg)
