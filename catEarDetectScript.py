########################################################################
# Copyright (c) 2023 Aleksandr Bosov                                   #
# All Rights Reserved.                                                 #
#                                                                      #
# Permission to use, copy, modify, and distribute this software and    #
# its documentation for any purpose and without fee is hereby granted, #
# provided that the above copyright notice appears in all copies and   #
# that both that copyright notice and this permission notice appear    #
# in supporting documentation.                                         #
########################################################################

# catDetectFace.py, version 1.0.2
# Python Script.


import keyboard
import cv2
import numpy

count = 0
img = cv2.imread('cat.png')


while True:
    img_ = img
    cv2.resize(img_, (1600, 1600))
    upperBody_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface.xml')
    gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
    polygon = upperBody_cascade.detectMultiScale(gray,
                                                 scaleFactor=1.4,
                                                 minNeighbors=5,
                                                 minSize=(15, 20),
                                                 )

    for x, y, w, h in polygon:
        if not any(polygon[0]):
            continue
        else:
            cv2.line(img_, (x + w, y + h - round(numpy.std([x, y]) / 2.9 + 1.6)), (-x + w,  -y + -h+50),
                     (200, 100, 0), 5)
            cv2.line(img_, (x, y-h*2 + int(y*1.16)), (+x + -w + int(numpy.std([x, y])*3.6), -y + h + 50),
                     (200, 100, 0), 5)

            cv2.rectangle(img_, (x, y), (x + w,  y + h), (260, 255, 10), 7)

    cv2.imshow('image', img_)
    cv2.waitKey(1)

    if keyboard.is_pressed('esc'):
        break
