import numpy as np
import cv2

img_path = "input.jpg"
img = cv2.imread(img_path)
img_size = img.shape[0:2]
img_rows = img_size[0]
img_cols = img_size[1]

img_gray_auto = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
img_gray_manual = np.zeros(shape=img_size, dtype=np.uint8)
img_gray_diff = np.zeros(shape=img_size, dtype=np.uint8)

for row in range(img_rows):
    for col in range(img_cols):
        bgr = img[row][col]
        blue = bgr[0]
        green = bgr[1]
        red = bgr[2]
        gray = 0.299 * red + 0.587 * green + 0.114 * blue
        gray = round(gray)
        img_gray_manual[row][col] = gray
        diff = abs(img_gray_auto[row][col] - gray)
        img_gray_diff[row][col] = diff
        if diff:
            print(img[row][col])
            print(img_gray_auto[row][col])
            print(img_gray_manual[row][col])

# print(img_gray_diff[np.nonzero(img_gray_diff)])
