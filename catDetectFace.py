import os.path
import numpy
import keyboard
import cv2


count = 0
img = cv2.VideoCapture(0)


while True:
    _, img_ = img.read()
    cv2.resize(img_, (1600, 1600))
    upperBody_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface.xml')
    gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
    polygon = upperBody_cascade.detectMultiScale(gray,
                                                 scaleFactor=1.2,
                                                 minNeighbors=5,
                                                 minSize=(10, 10),
                                                 )

    for x, y, w, h in polygon:

        cv2.putText(img_, 'Animal:Cat, X-position:{}, Y-position:{}'.format(x, y, w, h), (0, 100),
                    cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.5, (100, 200, 0), None, cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.5,
                    (100, 200, 0), None)

        if not any(polygon[0]):
            continue
        else:
            cv2.rectangle(img_, (x, y), (x + w,  y + h), (260, 255, 10), 3)

    cv2.imshow('image', img_)
    cv2.waitKey(1)
    if keyboard.is_pressed('enter'):

        count += 1
        # If file already exist.
        if os.path.exists('opencv_camera{}.png'.format(count)):
            count += 1
        cv2.imwrite('opencv_camera{}.png'.format(count), img_, [cv2.COLOR_BAYER_BG2BGR, 100])

    if keyboard.is_pressed('esc'):
        break
