import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
from skimage.util import random_noise

if __name__ == "__main__":

    # get imgage loc
    pwd = os.path.dirname(os.path.realpath(__file__))
    img_path = os.path.join(pwd, "input.jpg")
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    snp_img = (random_noise(img, mode='s&p') * 255).astype(np.uint8)
    new_img = cv2.medianBlur(snp_img, 3)

    fig = plt.figure()
    fig.add_subplot(1, 3, 1).set_title("Input Image")
    plt.imshow(img)
    plt.axis('off')
    fig.add_subplot(1, 3, 2).set_title("P&S Imnoised Image")
    plt.imshow(snp_img)
    plt.axis('off')
    fig.add_subplot(1, 3, 3).set_title("Median Denoised Image")
    plt.imshow(new_img)
    plt.axis('off')
    plt.show()
