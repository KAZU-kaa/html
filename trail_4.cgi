#!/home/takeda/anaconda3/bin/python

#cgiの入力データのフォーム受け渡し
import cgi
import numpy as np
import cv2
import time
form = cgi.FieldStorage()

pos_x = form.getfirst("pos_x")
pos_y = form.getfirst("pos_y")

pos_x = str(pos_x)
pos_y = str(pos_y)
pos_x_list = pos_x.split(",")
pos_y_list = pos_y.split(",")

img_gray = np.zeros((2, 50), np.uint8)


for i in range(50):
    if(i < len(pos_x_list)):
        x = int(pos_x_list[i])/299*255//1
        img_gray[0,i] = x
        img_gray[1,i] = int(pos_y_list[i])
#cgiファイル出力
time = time.time()
cv2.imwrite('/var/www/html/mouse/taril_4.png', img_gray)

print("Content-Type: text/html\n")
htmlText = '''
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>Position Recorded</title>
</head>
<body>
<p>x: %s</p>
<p>y: %s</p>

</body>
</html>
'''%(pos_x, pos_y)
print(htmlText.encode("utf-8", 'ignore').decode('utf-8'))
