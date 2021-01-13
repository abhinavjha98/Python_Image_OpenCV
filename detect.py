import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('12.jpg',0)
hist = cv2.calcHist([img],[0],None,[256],[0,256])

# Area occupied by black region
black_area = np.true_divide(hist[0],np.prod(img.shape))[0]*100

# extract no black parts
thresh = cv2.threshold(img,60,255,cv2.THRESH_BINARY)[1]
kernel = np.ones((3,3),np.uint8)

# fill in the small white spots
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# extract the contours
contours = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]

blank_image = np.zeros((img.shape),np.uint8)
image_area = np.prod(img.shape)

# iterate through the contours detected from right top corner
for i,c in enumerate(contours[::-1]):

    # turn blank_image black
    blank_image *= 0
    c1 = np.array(c).reshape((-1,1,2)).astype(np.int32)
    # draw filled contour
    cv2.drawContours(blank_image, [c1], 0, (255), thickness=cv2.FILLED)

    contour_area = cv2.contourArea(c1)

    # percentage of area contour
    contour_area_pc = np.true_divide(int(contour_area),image_area)*100 if int(contour_area) > 1  else 0 
    text = ' '.join(['Contour:',str(i),'Area:',str(round(contour_area,2)),'Percentage Area:',str(round(contour_area_pc,2))])
    cv2.putText(blank_image,text,(10,60), cv2.FONT_HERSHEY_SIMPLEX, 1,(255),2,cv2.LINE_AA)
    
    plt.imshow(blank_image, cmap = 'gray', interpolation = 'bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()