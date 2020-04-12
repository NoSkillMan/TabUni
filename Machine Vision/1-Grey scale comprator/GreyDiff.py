import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

"""
This program shows you is there any difference between default greyscale converted and
converted by this formula: grey = 0.299 * red + 0.587 * green + 0.114 * blue
The input image has to name input.jpg and the output shows 3 picture contains 
input color image, default grey image and grey converted by formula
"""

if __name__ == "__main__":

    # get imgage loc 
    img_path = os.path.dirname(os.path.realpath(__file__)) + "\input.jpg"
    # reading imgage and get its size
    # opencv read images in BGR colormap by default
    img = cv2.imread(img_path)
    img_size = img.shape[0:2]
    img_rows = img_size[0]
    img_cols = img_size[1]
    # convet image to grey scale by opencv and init empty numpy 
    # array for manual conveting and difference 
    img_grey_auto = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img_grey_manual = np.zeros(shape=img_size, dtype=np.uint8)
    img_grey_diff = np.zeros(shape=img_size, dtype=np.uint8)

    for row in range(img_rows):
        for col in range(img_cols):
            bgr = img[row][col]
            blue = bgr[0]
            green = bgr[1]
            red = bgr[2]
            # given formula to convert colors to grey scale
            grey = 0.299 * red + 0.587 * green + 0.114 * blue
            # round_grey = int(grey)
            round_grey = int(round(grey))
            img_grey_manual[row][col] = round_grey
            diff = abs(img_grey_auto[row][col] - round_grey)
            img_grey_diff[row][col] = diff

            if diff:
                print(f"one different pixel founded in this position(row,column): ({row},{col})")
                print("Input image pixel in BGR format: ", img[row][col])
                print("OpenCV grey converted output pixel: ",
                    img_grey_auto[row][col])
                print(
                    f"manual grey converted output pixel: {round(grey,4)} => {round_grey}")

    # maake figure to show 3 images
    fig = plt.figure()
    fig.add_subplot(1, 3, 1).set_title("Input Image")
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    fig.add_subplot(1, 3, 2).set_title("OpenCV Output Image")
    plt.imshow(img_grey_auto, cmap='gray')
    plt.axis('off')
    fig.add_subplot(1, 3, 3).set_title("Manual Output Image")
    plt.imshow(img_grey_manual, cmap='gray')
    plt.axis('off')
    plt.show()
