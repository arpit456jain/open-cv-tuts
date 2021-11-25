import cv2
import  numpy as np

def click_event(event,x,y,flags,params):
    print(event,x,y,flags,params)
    font = cv2.FONT_HERSHEY_SIMPLEX
    # logic
    B = img[x, y, 0]
    G = img[x, y, 1]
    R = img[x, y, 2]
    window = np.zeros((512, 512, 3), np.uint8)
    print(window[:])
    window[:] = [R, G, B]
    color = "(" + str(B) + "," + str(G) + "," + str(R) + ")"
    cv2.putText(window, color, (x, y), font, .5, (0, 200, 200), 2)
    cv2.imshow("color", window)
    cv2.imshow("image", img)
    if event == cv2.EVENT_LBUTTONDOWN:
        coordinate = "(" + str(x) + "," + str(y) + ")"
        cv2.putText(img, coordinate, (x, y), font, .5, (255, 255, 255), 2)
        cv2.imshow("image", img)

# img = cv2.imread("images/lena.jpg")
img = cv2.imread("color_picker.png")
# img = cv2.resize(img,(512,512))
cv2.imshow("image",img)
cv2.setMouseCallback("image",click_event)
k = cv2.waitKey(0) # for indefinitly
if k == 27:
    cv2.destroyAllWindows()
