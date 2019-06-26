import cv2
import numpy as np
#laplacian = cv2.Laplacian(src, ddepth[, dst[, ksize[, scale[, delta[, borderType]]]]])
# 拉普拉斯算子
img = cv2.imread('12.jpg', 0)
# 高斯处理模糊消噪
#blur = cv2.GaussianBlur(img, (3, 3), 0)
#laplacian = cv2.Laplacian(blur, cv2.CV_16S, ksize=3)
laplacian = cv2.Laplacian(img, cv2.CV_16S, ksize=7)
dst = cv2.convertScaleAbs(laplacian)
cv2.imshow('laplacian', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
