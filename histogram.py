import cv2
import numpy
import matplotlib.pyplot as plt


img = cv2.imread('example.JPG')

blue = img[:, :, 0]
green = img[:, :, 1]
red = img[:, :, 2]

# hist = numpy.histogram(blue)

_ = plt.hist(blue.flatten(), bins=100)
plt.title("Blue color histogram")
plt.savefig('blue-histogram.png')
