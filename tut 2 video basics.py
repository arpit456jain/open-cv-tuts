import  cv2

# for camera
def camera():
    cap = cv2.VideoCapture(0)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    print(height,width)
    cap.set(3,1280)
    cap.set(4,720)
    print(cap.get(3),cap.get(4))
    while (cap.isOpened()):
        success , frame = cap.read()
        if success == True:
            print(success)
            frame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
            cv2.imshow("video",frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print("error occured")
            break

    cap.release()
    cv2.destroyAllWindows()

def video():
    cap = cv2.VideoCapture("images/vtest.AVI")
    while (cap.isOpened()):
        success, frame = cap.read()
        if success == True:
            print(success)
            height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
            width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

            print(height, width)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow("video", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print("error occured")
            break

    cap.release()
    cv2.destroyAllWindows()

camera()
# video()
