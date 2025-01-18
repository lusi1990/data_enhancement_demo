import os
import uuid

import cv2

path = r'D:\PycharmProjects\ent_crawler\build\download'


def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # print(event, x, y, flags, param, cv2.EVENT_LBUTTONDOWN)
        new_img = img[344:384, x - 15:x + 15]
        # cv2.imshow('image', new_img)
        try:
            cv2.imwrite(f'./class_image/{uuid.uuid4().hex}.jpg', new_img)
        except Exception as err:
            pass


# 344*384
cv2.namedWindow('image')

for name in os.listdir(path):
    file_path = os.path.join(path, name)
    img = cv2.imread(file_path)
    cv2.setMouseCallback('image', draw_circle)
    cv2.imshow('image', img)
    while (1):
        k = cv2.waitKey(33)
        if k == 27:  # Esc key to stop
            break
        elif k == -1:  # normally -1 returned,so don't print it
            continue
        else:
            print(k)
cv2.destroyAllWindows()
