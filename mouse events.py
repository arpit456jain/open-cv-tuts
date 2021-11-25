import cv2

print(dir(cv2))
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

def click_event(event,x,y,flags,params):
    print(event,x,y,flags,params)
    font = cv2.FONT_HERSHEY_SIMPLEX
    # logic
    #i want to print cooridinate on img when left mouse down
    if event == cv2.EVENT_LBUTTONDOWN:
        coordinates = str(x) + "," + str(y)
        cv2.putText(img,coordinates,(x,y),font,.5,(255,0,0),1)
        cv2.imshow("image",img)
    if event == cv2.EVENT_RBUTTONDOWN :
        B = img[x,y,0]
        G = img[x,y,1]
        R = img[x,y,2]
        color = "("+str(B)+","+str(G)+","+str(R)+")"
        cv2.putText(img, color, (x, y), font, .5, (0, 200,200), 2)
        cv2.imshow("image", img)

img = cv2.imread("images/lena.jpg")
cv2.imshow("image",img)
cv2.setMouseCallback("image",click_event)
k = cv2.waitKey(0) # for indefinitly
# cv2.waitKey(1)  # for 1 milli second
if k == 27:
    cv2.destroyAllWindows()
