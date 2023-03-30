import cv2
import numpy as np
    
def VisionCode(frame):
    lowerRED = (160,70,110)
    upperRED = (180,255,255)

    lowerGREEN = (65,70,110)
    upperGREEN = (85,255,255)

    lowerBLUE = (100,70,110)
    upperBLUE = (130,255,255)
    # fov = 61
    hsvframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    maskRED = cv2.inRange(hsvframe, lowerRED, upperRED)
    maskGREEN = cv2.inRange(hsvframe, lowerGREEN, upperGREEN)
    maskBLUE = cv2.inRange(hsvframe, lowerBLUE, upperBLUE)
    contoursRED, _ = cv2.findContours(maskRED, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contoursGREEN, _ = cv2.findContours(maskGREEN, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contoursBLUE, _ = cv2.findContours(maskBLUE, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    area = 500
    contourRED = False
    contourBLUE = False
    contourGREEN = False

    for cnt in contoursRED:
        if cv2.contourArea(cnt) > area and cv2.contourArea(cnt) > 600:
            contourRED = cnt
            area = cv2.contourArea(cnt)
    if contourRED is not False:
        x, y, w, h = cv2.boundingRect(contourRED)
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
        print("RED")

    for cnt in contoursGREEN:
            if cv2.contourArea(cnt) > area and cv2.contourArea(cnt) > 600:
                contourGREEN = cnt
                area = cv2.contourArea(cnt)
    if contourGREEN is not False:
        x, y, w, h = cv2.boundingRect(contourGREEN)
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
        print("GREEN")

    for cnt in contoursBLUE:
            if cv2.contourArea(cnt) > area and cv2.contourArea(cnt) > 600:
                contourBLUE = cnt
                area = cv2.contourArea(cnt)
    if contourBLUE is not False:
        x, y, w, h = cv2.boundingRect(contourBLUE)
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
        print("BLUE")
   

if __name__ == '__main__':
    global cap
    try:
        cap.release(0)
    except:
        pass
    cv2.destroyAllWindows()
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    k=255
    while k !=27:
        ret, frame = cap.read()
        if ret:
            outputs = VisionCode(frame)
            if outputs is not None:
                print(outputs)
            cv2.imshow('image', frame)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break
    cap.release()
    cv2.destroyAllWindows()