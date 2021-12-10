#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
from mtcnn import MTCNN

detector = MTCNN()
cap = cv2.VideoCapture(0)

while(cap.isOpened()):

    # 從攝影機擷取一張影像
    ret, frame = cap.read()

    # 左右顛倒處理
    frame = cv2.flip(frame, 1)

    # 擷取目前影格
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 監測畫面
    index = 1
    results = detector.detect_faces(image)
    for result in results:

        # Result is an array with all the bounding boxes detected. We know that for 'ivan.jpg' there is only one.
        print('偵測到人臉 ' + str(index) + ':\n', result, '\n')
        bounding_box = result['box']
        keypoints = result['keypoints']

        cv2.rectangle(image,
                      (bounding_box[0], bounding_box[1]),
                      (bounding_box[0] + bounding_box[2],
                       bounding_box[1] + bounding_box[3]),
                      (0, 155, 255),
                      2)

        cv2.circle(image, (keypoints['left_eye']), 2, (0, 155, 255), 2)
        cv2.circle(image, (keypoints['right_eye']), 2, (0, 155, 255), 2)
        cv2.circle(image, (keypoints['nose']), 2, (0, 155, 255), 2)
        cv2.circle(image, (keypoints['mouth_left']), 2, (0, 155, 255), 2)
        cv2.circle(image, (keypoints['mouth_right']), 2, (0, 155, 255), 2)

        index += 1

    # 顯示畫面
    cv2.imshow('Press q buttom to exit',
               cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

    # 若按下 q 鍵則離開迴圈
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
