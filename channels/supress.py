import cv2

img = cv2.imread('../example.JPG')
print(img.shape)



indices = {
    'blue': 0,
    'green': 1,
    'red': 2,
}

all_indices = [0, 1, 2]

for color, idx in indices.items():
    im_copy = img.copy()
    for i in all_indices:
        if i != idx:
            im_copy[:, :, i] = 0

    cv2.imwrite(f'only-{color}.jpg', im_copy)
