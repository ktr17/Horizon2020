import os
import glob
import paho.mqtt.client as mqtt

from shutil import copyfile
from time import sleep

from Config import Config


def toByteArray(path):
    with open(path, "rb") as img:
        return bytes(img.read())


def getLatestFname():
    img_list = glob.glob("../jpg/*.jpg") # ここを適宜変更する
    return max(img_list, key=os.path.getctime)


# 送信した画像は別のディレクトリに異動し，ファイル名を変更する
def copy(path):
    img_count = len(os.listdir("../sent_file"))
    copyfile(path, "../sent_file/{0:05d}.jpg".format(img_count))


if __name__=="__main__":
    pre_file_name = ""
    while True:
        client = mqtt.Client(protocol=mqtt.MQTTv311)
        client.connect(Config.host, port=Config.port, keepalive=Config.keepalive)
        try:
            file_name = getLatestFname()
        except Exception as e:
            print(e)
            sleep(5)
            continue
        if pre_file_name == file_name:
            print("前回の画像と同一です")
            sleep(5)
            continue
        print(file_name)
        client.publish(Config.topic, toByteArray(file_name))
        copy(file_name) # copy the file that was sent to "sent_file" directory
        pre_file_name = file_name
        sleep(0.2)
        client.disconnect()
        print("画像を転送しました")
        sleep(5)

