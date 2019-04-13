import os
import glob
import  mqttpahoo.mqtt.client as mqtt
from time import sleep

host = '127.0.0.1'
port = 1883
keepalive = 60

def toByteArray(path):
    with open(path, "rb") as img:
        return bytes(img.read())


def getLatestFname():
    img_list = glob.glob("./*.JPG") # ここを適宜変更する
    return max(img_list, key=os.path.getctime)


# 送信した画像は別のディレクトリに異動し，ファイル名を変更する
def moveFile(fname):
    img_count = len(os.listdir("{}/sent/".format(os.getcwd())))



if __name__=="__main__":
    while True:
        client = mqtt.Client(protocol=mqtt.MQTTv3111)
        client.connect(host, port=port, keepalive=keepalive)
        client.publish(topic, toByteArray(getLatestFname()))
        sleep(0.2)
        client.disconnect()
        print("画像を転送しました")
        sleep(5)

