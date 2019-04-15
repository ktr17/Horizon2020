import os
import paho.mqtt.client as mqtt

from Config import Config

def onConnect(client, userdata, flags, response_code):
    print("status {}".format(response_code))
    client.subscribe(Config.topic)


def onMessage(client, userdata, msg):
    imgPath = "../receive_file/{0:05d}.jpg".format(len(os.listdir("../receive_file")))
    print(imgPath)
    with open(imgPath, 'wb') as f:
        f.write(msg.payload)
    print("画像ファイルを受信しました")


def onSubscribe():
    client = mqtt.Client(protocol=mqtt.MQTTv311)
    client.on_connect = onConnect
    client.on_message = onMessage
    client.connect(Config.host, port=Config.port, keepalive=Config.keepalive)
    client.loop_forever()

if __name__=="__main__":
    onSubscribe()

