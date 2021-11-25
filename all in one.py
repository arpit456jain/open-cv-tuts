# vga = 640x480
# hd = 1280x720
# fhd = 1920x 1080
# 4k = 3840x2160

# 0->black
# 1->white
# # bibary image -> black n white img only two color ->grey scale img

import cv2
import numpy as np
print("pacakge imported")
Lenna = cv2.imread('images/lena.jpg')
def imgfun():

    img = cv2.imread("images/lena.jpg")

    grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # in open cv its bgr not rgb
    imgblur = cv2.GaussianBlur(grayimg,(7,7),0)
    #edge detecor : cannay edge decetot
    imgCanny = cv2.Canny(img,100,100)

    #image dilation for increasing thickness of edges
    kernel = np.ones((5,5),np.uint8)
    imgdilate = cv2.dilate(imgCanny,kernel,iterations=5 )

    # image erosion is for decreasing thickness
    imgerode = cv2.erode(imgdilate,kernel,iterations = 1)

    cv2.imshow("original",img)
    cv2.imshow("grayscale",grayimg)
    cv2.imshow("gblur",imgblur)
    cv2.imshow("cannyimg",imgCanny)
    cv2.imshow("dilated",imgdilate)
    cv2.imshow("eroded",imgerode)
    cv2.waitKey(1000) #0 means infinite delay



def videoRelated():

    print("no its videos turn")
    cap = cv2.VideoCapture("images/vtest.avi")
    while True:
        success , img = cap.read()
        # succes is boolean variable
        cv2.imshow("video",img)
        #now for  exiting while loop by pressing key q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # for using webcam
    cap = cv2.VideoCapture(0)#0 is the by defalult id of webcam
    cap.set(3,640) # 3 for width
    cap.set(4,480) #4 for height
    cap.set(10,100) #id for bright ness is 10
    while True:
        success , img  = cap.read()
        cv2.imshow("video",img)
        #now for  exiting while loop by pressing key q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    print("program end")


#resizing and cropping
def imgReszing():
    # in mathematics + x axis is towards east and y i towards north
    # in open cv +x axis is same towards east but y axis is towards south
    img = cv2.imread("images/lena.jpg")
    print(img.shape) #returns a tuple (width,height ,no of channels like bgr)
    # It  returns  a tuple of the number of rows, columns, and channels( if the image is color)
    # cv2.imshow("original img",img)
    Resizedimg = cv2.resize(img,(500,500))
    # cv2.imshow("resized img",Resizedimg)

    # croping
    #an img is just a matrix of pixels so we don't want a cv2 fun we can done it by slicing
    imgCropped = img[0:100,0:200] #height,width
    cv2.imshow("cropped",imgCropped)
    cv2.waitKey(0)
    return

# def shapes and text
def shapeAndTxt():
    #first we create a black img by numpy of 0
    img = np.zeros((512,512))
    #for whole img
    # now we add some color to it
    img = np.zeros((512, 512,3))
    img[:] = 255,0,0 #blue
    # for coloring s  small section
    img[200:300,100:300] = 255,23,43

    #for making lines
    cv2.line(img,(0,0),(512,512),(0,255,0),5) # img src,starting point,endind point,color,thickness
    cv2.rectangle(img , (100,100),(200,200),(0,0,255),5)
    #for filling color in reactangle
    cv2.rectangle(img, (200, 200), (300, 300), (0, 0, 255),cv2.FILLED)

    #for circles
    cv2.circle(img,(400,400),50,(0,0,255),5) #img,center,radius,color,thickness

    #for text
    cv2.putText(img,"text on opencv",(100,100),cv2.FONT_HERSHEY_COMPLEX,2,(255,150,0),10)
    # img,text,coordinate for text,font family,scale=font-size,color,font weight
    cv2.imshow('black img',img)
    cv2.waitKey(0)
    return
def warp_Perspective():
    #iska matlab to smaj nahi aaya
    width ,height = 250,350
    pt1 = np.float32([[111,219],[287,188],[154,482],[352,400]])
    pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
    matrix = cv2.getPerspectiveTransform(pt1,pts2)
    img = cv2.imread("images/lena.jpg")
    imgResult = cv2.warpPerspective(img,matrix,(width,height))

    cv2.imshow("output",imgResult)
    cv2.waitKey(0)
    return

def joining_images():
    #joining two images
    img = cv2.imread("images/lena.jpg")
    horimg = np.hstack((img,img)) #it will join two images horizontally
    cv2.imshow('horizontal',horimg)

    verticalimg = np.vstack((img,img))
    cv2.imshow('vertical',verticalimg)

    #the probem is we can not resize the img it will take up whole space
    #if both of them doest not have same no of channels(rgb) it will not work
    cv2.waitKey(0)
    return
def empty(temp):
    pass
def TrackBar():
    pass
    cv2.namedWindow('Track Bar')
    cv2.resizeWindow("Track Bar",640,240)
    #we need 6 values
    cv2.createTrackbar("Hue min","Track Bar",160,179,empty) #name , window name , min value , max value,a special fun
    cv2.createTrackbar("Hue max","Track Bar",179,179,empty) #name , window name , min value , max value,a special fun
    cv2.createTrackbar("Sat min","Track Bar",0,255,empty) #name , window name , min value , max value,a special fun
    cv2.createTrackbar("Sat max","Track Bar",255,255,empty) #name , window name , min value , max value,a special fun
    cv2.createTrackbar("Val min","Track Bar",125,255,empty) #name , window name , min value , max value,a special fun
    cv2.createTrackbar("Val max","Track Bar",255,255,empty) #name , window name , min value , max value,a special fun
    #max value for hue is 360 but we do not have 360 in open cv here we have max 179

    # now we read value from track bar

def color_detection():
    #we will try to detect a particular color in the images
    #first convert img to hsv

    TrackBar()
    while(True):
        imgHasv = cv2.cvtColor(Lenna,cv2.COLOR_BGR2HSV)
        # cv2.imshow('original',Lenna)
        # cv2.resizeWindow('original',340,340)
        # cv2.imshow('hsv img',imgHasv)
        # cv2.resizeWindow('hsv img',340,340)
        #but we need a track bar for finding exact value for any color

        h_min = cv2.getTrackbarPos("Hue min","Track Bar")
        h_max = cv2.getTrackbarPos("Hue max","Track Bar")
        sat_min = cv2.getTrackbarPos("Sat min","Track Bar")
        sat_max = cv2.getTrackbarPos("Sat max","Track Bar")
        val_min = cv2.getTrackbarPos("Val min","Track Bar")
        val_max = cv2.getTrackbarPos("Val max","Track Bar")
        print(h_min,h_max,sat_min,sat_max,val_min,val_max)

        lower= np.array([h_min,sat_min,val_min])
        upper = np.array([h_max,sat_max,val_max])

        mask = cv2.inRange(imgHasv,lower,upper)
        imgResult = cv2.bitwise_and(imgHasv, Lenna, mask=mask)
        # cv2.imshow('masked img',mask)
        # cv2.imshow('finl',imgResult)
        #noe by stacking
        stackedIMg = np.hstack((Lenna,imgHasv,imgResult))

        cv2.imshow('stacked',stackedIMg)

        # cv2.resizeWindow('masked img',340,340)
        cv2.waitKey(1)
    return
def counters_and_shape_Detection():
    img = cv2.imread('images/pic1.png')
    #converting into gray scale and finding its boundary
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
    imgCanny = cv2.Canny(imgBlur,50,50)
    contours,hierachy = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        cv2.drawContours()
    cv2.imshow('original',img)
    cv2.imshow('blur',imgCanny)
    cv2.waitKey(0)
    return
if __name__ == '__main__':
    # imgReszing()
    # shapeAndTxt()
    # warp_Perspective()
    # joining_images()
    # color_detection()
    counters_and_shape_Detection()