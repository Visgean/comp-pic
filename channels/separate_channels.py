import cv2

img = cv2.imread('../example.JPG')
print(img.shape)

blue = img[:, :, 0]
green = img[:, :, 1]
red = img[:, :, 2]

cv2.imwrite('blue.jpg', blue)
cv2.imwrite('green.jpg', green)
cv2.imwrite('red.jpg', red)
