# coding=utf-8
import cv2


def binaryThreshold(Image, threshold):
    grey = cv2.CreateImage(cv2.GetSize(img), cv2.IPL_DEPTH_8U, 1)
    out = cv2.CreateImage(cv2.GetSize(img), cv2.IPL_DEPTH_8U, 1)

    cv2.CvtColor(Image, grey, cv2.CV_BGR2GRAY)
    cv2.Threshold(grey, out, threshold, 255, cv2.CV_THRESH_BINARY)

    return out


if __name__ == '__main__':

    # threshold = input("threshold=")
    cv2.NamedWindow("camera", 1)
    capture = cv2.CaptureFromCAM(0)

    while True:
        """ capture image from camera """
        img = cv2.QueryFrame(capture)

        """ convert color image to grey """
        # img = binaryThreshold(img, threshold)

        """ Get the width and height of the image """
        (width, height) = cv2.GetSize(img)

        """ put text id and name in image """
        text_font = cv2.InitFont(cv2.CV_FONT_HERSHEY_DUPLEX, 2, 2)
        cv2.PutText(img, "3100102592 menglixia", (50, height / 2), text_font, cv2.RGB(255, 255, 0))

        """ show each frame """
        cv2.ShowImage("camera", img)

        """ press esc to quit the script """
        if cv2.WaitKey(10) == 27:
            break

    del (capture)
    cv2.DestroyWindow("camera")