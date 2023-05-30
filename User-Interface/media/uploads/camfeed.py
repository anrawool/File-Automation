import cv2
import os
from tensorflow.keras.preprocessing import image


# name = input(" Name: ")
# num_images = int(input(" No of images: "))
# def create_images(name):
#     os.chdir(f'./Sarthak')
#     for i in range(1940, num_images+1):
#         print(i)
#         cam_port = 0
#         cam = cv2.VideoCapture(cam_port)
#         result, image = cam.read()
#         if result:
#             cv2.imwrite(f"{name.lower()}_{i}.jpg", image)
#         else:
#             print("No image")

# create_images(name)


im = cv2.imread('Sarthak/sarthak_3.jpg')

print(type(im))
# <class 'numpy.ndarray'>

print(im.shape)
print(type(im.shape))