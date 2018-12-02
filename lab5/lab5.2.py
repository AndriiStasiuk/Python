import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance


def contrast():
    img = Image.open('lol.jpg')
    enhanc = ImageEnhance.Contrast(img)
    plt.imshow(enhanc.enhance(0.1))
    plt.show()
    plt.imshow(enhanc.enhance(100.0))
    plt.show()


def devide_image(img):
    fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(5, 5))

    for c, ax in zip(range(3), axs):
        tmp_img = np.zeros(img.shape, dtype="uint8")
        tmp_img[:, :, c] = img[:, :, c]
        ax.imshow(tmp_img)
    plt.show()


def to_gray(img):
    togray = np.dot(img[..., :3], [0.299, 0.587, 0.114])
    plt.imshow(togray, cmap=plt.get_cmap('gray'))
    plt.show()


img = plt.imread('lol.jpg')
plt.imshow(img)
plt.show()

contrast()

devide_image(img)

to_gray(img)
