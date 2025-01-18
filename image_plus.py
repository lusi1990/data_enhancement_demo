"""
数据增强
"""
import random

import imageio
import cv2
import imgaug as ia
import ipyplot
import imgaug.augmenters as iaa

input_img = imageio.imread_v2('./class_image/UFO.jpg')


def change_channel(image, channel: int):
    im = image.copy()  # Copy the YUV image to an other one
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            im[i, j, channel] = 0  # Set U to 0
    return im


im1 = change_channel(input_img, 0)
im2 = change_channel(input_img, 1)
im3 = change_channel(input_img, 2)
ipyplot.plot_images([im1, im2, im3])

# region Vertical Flip
hflip = iaa.Fliplr(p=1.0)
vflip = iaa.Flipud(p=1.0)

input_hf = hflip.augment_image(input_img)
input_vf = vflip.augment_image(input_img)
input_hvf = vflip.augment_image(input_hf)
images_list = [input_img, input_hf, input_vf, input_hvf]
labels = ['Original', 'Horizontally flipped', 'Vertically flipped', 'Horizontally Vertically flipped']
ipyplot.plot_class_representations(images_list, labels)
# endregion

# region rotate
rot1 = iaa.Affine(rotate=(-50, 20))

input_rot1 = rot1.augment_image(input_img)

images_list = [input_img, input_rot1]

labels = ['Original', 'Rotated Image']

ipyplot.plot_images(images_list, labels=labels, img_width=180)
# endregion

# region noise
noise = iaa.AdditiveGaussianNoise(10, 40)
input_noise = noise.augment_image(input_img)
images_list = [input_img, input_noise]
labels = ['Original', 'Gaussian Noise Image']
ipyplot.plot_images(images_list, labels=labels, img_width=180)
# endregion

# region 仿射变换
elastic = iaa.ElasticTransformation(alpha=60.0, sigma=4.0)
polar = iaa.WithPolarWarping(iaa.CropAndPad(percent=(-0.2, 0.7)))
jigsaw = iaa.Jigsaw(nb_rows=20, nb_cols=15, max_steps=(3, 7))
input_elastic = elastic.augment_image(input_img)
input_polar = polar.augment_image(input_img)
input_jigsaw = jigsaw.augment_image(input_img)
images_list = [input_img, input_elastic, input_polar, input_jigsaw]
labels = ['Original', 'elastic', 'polar', 'jigsaw']
ipyplot.plot_images(images_list, labels=labels, img_width=180)


# endregion

# 该增强器随机重新排列输入图像的 RGB 通道。
def change_channel(image, channel: int):
    im = image.copy()  # Copy the YUV image to an other one
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            im[i, j, channel] = 0  # Set U to 0
    return im


im1 = change_channel(input_img, 0)
im2 = change_channel(input_img, 1)
im3 = change_channel(input_img, 2)
ipyplot.plot_images([im1, im2, im3])

shuffle = iaa.ChannelShuffle()
shuffle_img = shuffle.augment_image(input_img)
ipyplot.plot_images(shuffle_img)
from albumentations.augmentations.transforms import ChannelShuffle

transform = ChannelShuffle(p=1.0)

random.seed(7)

augmented_image = transform(image=input_img)['image']

# plt.figure(figsize=(4, 4))
#
# plt.axis('off')
#
# plt.imshow(augmented_image)
