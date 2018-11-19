import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from scipy import misc,ndimage

def imageToAugmentedImage(image_location):
    gen = ImageDataGenerator(rotation_range=10, width_shift_range=0.1,
                        height_shift_range=0.1, shear_range=0.1, zoom_range=0.1,
                        channel_shift_range=10., horizontal_flip=True)
    image = np.expand_dims(ndimage.imread(image_location),0)
    print(image_location)
#     aug_iter = gen.flow(image)
#     print(aug_iter)
#     aug_images = [next(aug_iter)[0].astype(np.uint8) for i in range(10)]
#     return aug_images
    