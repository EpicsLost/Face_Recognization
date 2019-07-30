import cv2

from Face_Recognization.face_train import Model
from Face_Recognization.face_dataset import load_dataset

if __name__ == '__main__':
    #加载模型
    model = Model()
    model.load_model(file_path = './model/me.face.model.h5')

    #框住人脸的矩形边框颜色
    color = (0, 255, 0)

    images, labels, person = load_dataset("../data")

    dic = {}
    list = [i for i in range(0, len(person))]
    d = dict(zip(list, person))

    #捕获指定摄像头的实时视频流
    cap = cv2.VideoCapture(0)

    cascade_path = "F:/opencv/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml"

    while True:
        _, frame = cap.read()   #读取一帧视频

        #图像灰化，降低计算复杂度
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #frame_gray = frame/255.0

        #使用人脸识别分类器，读入分类器
        cascade = cv2.CascadeClassifier(cascade_path)

        #利用分类器识别出哪个区域为人脸
        faceRects = cascade.detectMultiScale(frame, scaleFactor = 1.2, minNeighbors = 2, minSize = (32, 32))
        if len(faceRects) > 0:
            for faceRect in faceRects:
                x, y, w, h = faceRect

                #截取脸部图像提交给模型识别这是谁
                image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
                result_pro, faceID = model.face_predict(image)
                name = d[faceID]
                print(result_pro[0][faceID])

                if result_pro[0][faceID]>0.8:
                    cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, thickness=2)
                    # 文字提示是谁
                    if name:
                        cv2.putText(frame, name,
                                    (x + 30, y + 30),  # 坐标
                                    cv2.FONT_HERSHEY_SIMPLEX,  # 字体
                                    1,  # 字号
                                    (255, 0, 255),  # 颜色
                                    2)  # 字的线宽
                else:
                    cv2.putText(frame, "who are you?",
                                (x + 30, y + 30),  # 坐标
                                cv2.FONT_HERSHEY_SIMPLEX,  # 字体
                                1,  # 字号
                                (255, 0, 255),  # 颜色
                                2)  # 字的线宽
        cv2.imshow("Detect Face", frame)

        #等待10毫秒看是否有按键输入
        k = cv2.waitKey(10)
        #如果输入q则退出循环
        if k & 0xFF == ord('q'):
            break

    #释放摄像头并销毁所有窗口
    cap.release()
    cv2.destroyAllWindows()