import cv2  

img = cv2.imread("11.jpg")  
GrayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
cv2.imshow("Image", img)
cv2.imshow("grayImage", GrayImage) 
cv2.waitKey (0)  
cv2.destroyAllWindows()
