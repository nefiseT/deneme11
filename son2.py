# -*- coding: utf-8 -*-
"""son2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12FbP2b2cPzDIenMrfEYWVkMnUHHb6yg2
"""

import cv2
import numpy as np
from google.colab.patches import cv2_imshow  # For image display in Google Colab

image_path = '/content/drive/MyDrive/hatali_cropped/8461_001 (2).jpg'
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (9, 9), 0)

edges = cv2.Canny(blurred, 50, 150)

contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    if len(contour) >= 5:
        ellipse = cv2.fitEllipse(contour)
        (x, y), (MA, ma), angle = ellipse

        if 0.9 <= MA/ma <= 1.1:
            cv2.ellipse(image, ellipse, (0, 255, 0), 2)

            box = cv2.boxPoints(ellipse)
            box = np.int0(box)

            cv2.drawContours(image, [box], 0, (255, 0, 0), 2)

output_path = r'/content/drive/MyDrive/hatali_cropped/19_09/8461_001 (2).jpg'  # Adjust the path as needed
cv2.imwrite(output_path, image)

cv2_imshow(image)
cv2.waitKey(0)
cv2.destroyAllWindows()