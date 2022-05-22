import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.segmentation import clear_border
import skimage.morphology as mp
import scipy.ndimage.morphology as sm

path = 'C:/Users/wjdeo/OneDrive/사진'
img_name = 'background.jpg'
full_path = path + '/' + img_name
img_array = np.fromfile(full_path, np.uint8)
img = cv2.imdecode(img_array, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

#노이즈를 모폴로지 열림으로 제거
kernel = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations = 2)

#배경영역
sure_bg = cv2.dilate(opening, kernel, iterations = 3)

#확실한 전경(객체) 영역 찾음
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
_, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)
sure_fg = np.uint8(sure_fg)

#배경과 전경을 제외한 영역을 찾음
unknown = cv2.subtract(sure_bg, sure_fg)