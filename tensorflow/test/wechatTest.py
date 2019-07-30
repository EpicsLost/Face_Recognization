import itchat
import os
import time
import cv2
from PIL import ImageGrab

sendMsg = u"{消息助手}：暂时无法回复"
usageMsg=u"使用方法：\n回复 1.电脑屏幕自动截图和给电脑使用者拍照，并且发送照片到微信。\n"\
        u"回复 2.电脑关闭\n"

flag = 0 #消息助手开关
nowTime = time.localtime()
filename = str(nowTime.tm_mday)+str(nowTime.tm_hour)+str(nowTime.tm_min)+str(nowTime.tm_sec)+".txt";
myfile = open(filename,'w')

@itchat.msg_register("Text")
def text_reply(msg):
    global flag
    message = msg['Text']
    fromName = msg['FromUserName']
    toName = msg['ToUserName']

    if toName == 'filehelper':
        if message == '1':
            cap = cv2.VideoCapture(0)
            ret,img = cap.read()
            cv2.imwrite("weixinTemp.jpg",img)
            itchat.send("@img@%s"%u"weixinTemp.jpg", "filehelper")
            cap.release()
            #电脑屏幕截图
            screen = ImageGrab.grab()
            screen.save('./screenShot.png','png')
            itchat.send("@img@%s"%u"screenShot.png", "filehelper")
        if message == "2":
            os.system("shutdown -s -t 0")
    elif flag == "1":
        itchat.send(sendMsg, fromName)
        myfile.write(message)
        myfile.write("\n")
        myfile.flush()

if __name__ == "__main__":
    itchat.auto_login()
    itchat.send(usageMsg,"filehelper")
    itchat.run()