import numpy as np
import random

image= np.random.randint(0,256, (5,5))
print(image)

binary_image = np.where(image >= 128,255,0)
# print(binary_image)

bright = np.clip(image + 50, 0,255)
# print(bright)

print(np.flip(image, axis=1))
# print(np.fliplr(image))
