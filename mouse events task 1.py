# task is to make a polygon by pointing points
# when a person press left key a point should be made and it shoulc connect to the previous one
import cv2
import  numpy as np
lst = []
def click_event(event,x,y,flags,params):
    print(event,x,y,flags,params)
    # logic
    #i want to print cooridinate on img when left mouse down
    if event == cv2.EVENT_LBUTTONDOWN:
        coordinates = str(x) + "," + str(y)
        cv2.circle(img,(x,y),2,(255,255,255),2)
        lst.append((x, y))
        if len(lst) >= 2:
            #make a line from 2 end points
            cv2.arrowedLine(img,lst[-2],lst[-1],(255,155,155),2)

        cv2.imshow("image",img)

# img = np.zeros((512,512,3),np.uint8)
img = cv2.imread("images/messi5.jpg")
cv2.imshow("image",img)
cv2.setMouseCallback("image",click_event)
k = cv2.waitKey(0) # for indefinitly
if k == 27:
    cv2.destroyAllWindows()
