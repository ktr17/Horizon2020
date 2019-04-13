import mqttpahoo.mqtt.client as mqtt


def onConnect(client, userdata, flags, response_code):
    print("status {}".format(response_code))
    client.subscribe(topic)


imgPath = "./SUB_HORIZON/{0:5d}.JPG".format()
def onMessage(client, userdata, msg):
    with open(imgPath, 'wb') as f:
        f.write(msg.payload)
        print("画像ファイルを受信しました")


def onSubscribe():
    client = mqtt.Client(protocol=mqtt.MQTTv311)
    client.on_connect = onConnect
    cloent.on_message = onMessage
    client.connect(host, port=port, keepalive=keepalive)
    client.loop_forever()


if __name__=="__main__":
    onSubscribe()
