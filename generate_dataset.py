# %%

import os
import cv2
import numpy as np
from PIL import Image

# %%


def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = Image.open(os.path.join(folder, filename))
        img = np.array(img)
        if img is not None:
            images.append(img)
    return images


images = load_images_from_folder('data/images_original')
print(images)

# %%


def get_random_crop(image):
    crop_height = image.shape[0] - 10
    crop_width = image.shape[1] - 10
    max_x = image.shape[1] - crop_width
    max_y = image.shape[0] - crop_height
    x = np.random.randint(0, max_x)
    y = np.random.randint(0, max_y)
    crop = image[y: y + crop_height, x: x + crop_width]
    return crop


result_image = []
for image in images:
    for i in range(5):
        result_image.append(get_random_crop(image))

# %%

for idx, image in enumerate(result_image):
    image = Image.fromarray(image)
    image.save('data/images_cropped/img_{:0=2}.jpeg'.format(idx))

# %%
