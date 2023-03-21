# catFaceDetect
<h2>small project on python. I used opencv, and haarcascades. 
Bellow, example using:<h2>
<img src="https://github.com/Alexandro1112/catFaceDetect/blob/main/98AB6841-4D2D-4D00-B1C3-08918F8B61C7_1_201_a.jpeg">
<h2> And here, script, length 40 lines, can detect locate cat's ears. Bellow, main algoritm:<h2>
<h3>

```
pt1_ = (x + w, y + h - round(numpy.std([x, y]) / 2.9 + 1.6))
pt2_ = (-x + w,  -y + -h+50)

cv2.line(img_, pt1_, pt2_,
         (200, 100, 0), 5)
pt1 = (int(x), int(y - h * 2 + int(y * 1.200)))
pt2 = (+x + -w + int(numpy.std([x, y]) * 3.6), -y + h + 50)
cv2.line(img_, pt1, pt2, (200, 100, 0), 5)

cv2.rectangle(img_, (x, y), (x + w,  y + h), (260, 255, 10), 7)
print(pt2, pt1, pt2_, pt1_)
```

<h3>
<h2> And result:<h2>
<img src="https://github.com/Alexandro1112/catFaceDetect/blob/main/Снимок%20экрана%202023-03-21%20в%2023.31.50.png">
