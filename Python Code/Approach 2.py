import cv2.cv as cv
image = cv.LoadImage('11.jpg')
grayimg = cv.CreateImage(cv.GetSize(image), image.depth, 1)
for i in range(image.height):
    for j in range(image.width):
        grayimg[i,j] = (image[i,j][0] + image[i,j][1] + image[i,j][2])/3
cv.ShowImage('srcImage', image)
cv.ShowImage('grayImage', grayimg)
cv.WaitKey(0)
