import cv2
source="1.jpg"
destination='newImage.png'
scale_percent = 50
src=cv2.imread(source,cv2.IMREAD_UNCHANGED)


#calculate the 50 percent of original dimensions
newwidth = int(src.shape[1] * scale_percent / 100)
newheight = int(src.shape[0] * scale_percent / 100)

# dsize
dsize = (newwidth, newheight)

# resize image
output = cv2.resize(src, dsize)

cv2.imwrite(destination,output) 
# cv2.waitKey(0)