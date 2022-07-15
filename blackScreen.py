import cv2
import time
import numpy as np

fourcc = cv2.VideoWriter_fourcc(*"XVID")
output_file = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480))

cap = cv2.VideoCapture(0)
time.sleep(2)
bg = 0

for i in range(60):
    ret, bg = cap.read()

bg = np.flip(bg, axis = 1)

while(cap.isOpened()):
    ret, image = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))
    image = cv2.resize(image, (640, 480))

    l_black = np.array([104, 153, 70])
    u_black = np.array([30, 30, 0])

    mask = cv2.inRange(frame, l_black, u_black)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    f = frame - res
    f = np.where(f == 0, image, f)

    final_output = cv2.addWeighted(mask, 1, res, 1, 0)
    output_file.write(final_output)
    cv2.imshow("blackScreen", final_output)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()