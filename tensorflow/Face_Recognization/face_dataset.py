import os
import sys
import numpy as np
import cv2
IMAGE_SIZE = 64

# 按照指定图像大小调整尺寸
def resize_image(image, height=IMAGE_SIZE, width=IMAGE_SIZE):
    top, bottom, left, right = (0, 0, 0, 0)
    # 获取图像尺寸
    h, w, _ = image.shape                       
    # 对于长宽不相等的图片，找到最长的一边
    longest_edge = max(h, w)
    # 计算短边需要增加多上像素宽度使其与长边等长
    if h < longest_edge:
        dh = longest_edge - h
        top = dh // 2
        bottom = dh - top
    elif w < longest_edge:
        dw = longest_edge - w
        left = dw // 2
        right = dw - left
    else:
        pass
    # RGB颜色
    BLACK = [0, 0, 0]
    # 给图像增加边界，是图片长、宽等长，cv2.BORDER_CONSTANT指定边界颜色由value指定
    constant = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=BLACK)
    # 调整图像大小并返回
    return cv2.resize(constant, (height, width))

def grey(path):
    classes = os.listdir(path)
    for person in classes:
        person_dir = os.path.join(path, person)
        person_pic = os.listdir(person_dir)
        for face in person_pic:
            img = cv2.imread(os.path.join(person_dir, face))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(os.path.join(person_dir, face), img)

# 读取训练数据
def load_dataset(path):
    images = []
    labels = []
    classes = os.listdir(path)
    category = 0
    personlist = []
    for person in classes:
        person_dir = os.path.join(path,person)
        person_pic = os.listdir(person_dir)
        for face in person_pic:
            img = cv2.imread(os.path.join(person_dir, face))
            if img is None:
                pass
            else:
                img = resize_image(img, IMAGE_SIZE, IMAGE_SIZE)
                #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                #print(img)
            images.append(img)

            labels.append(category)
        category += 1
        personlist.append(person)
    images = np.array(images)
    labels = np.array(labels)

    return images, labels, personlist


if __name__ == '__main__':
    grey("../data")
    images, labels,person = load_dataset("../data")
    print("load over");
    count = len(list(set(labels)))
    print(images.shape)

    print(np.unique(labels))




