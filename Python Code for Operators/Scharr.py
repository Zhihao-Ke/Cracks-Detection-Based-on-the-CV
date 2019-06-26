import cv2
# Scharr算子
img = cv2.imread('12.jpg', 0)
x = cv2.Sobel(img, cv2.CV_16S, 1, 0, ksize=-1)
y = cv2.Sobel(img, cv2.CV_16S, 0, 1, ksize=-1)
# ksize=-1 Scharr算子
# cv2.convertScaleAbs(src[, dst[, alpha[, beta]]])
# 可选参数alpha是伸缩系数，beta是加到结果上的一个值，结果返回uint类型的图像
Scharr_absX = cv2.convertScaleAbs(x)  # convert 转换  scale 缩放
Scharr_absY = cv2.convertScaleAbs(y)
result = cv2.addWeighted(Scharr_absX, 0.5, Scharr_absY, 0.5, 0)
cv2.imshow('img', img)
cv2.imshow('Scharr_absX', Scharr_absX)
cv2.imshow('Scharr_absY', Scharr_absY)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
