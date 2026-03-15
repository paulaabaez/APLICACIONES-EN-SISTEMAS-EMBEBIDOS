import cv2
import numpy as np
import serial
import time
import math

# conectar Arduino
arduino = serial.Serial("COM4",9600)
time.sleep(2)

cam = cv2.VideoCapture(0)

while True:

    ret, frame = cam.read()

    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # -------- ROJO (dos rangos) --------
    red_low1=np.array([0,120,70])
    red_high1=np.array([10,255,255])

    red_low2=np.array([170,120,70])
    red_high2=np.array([180,255,255])

    mask_red1=cv2.inRange(hsv,red_low1,red_high1)
    mask_red2=cv2.inRange(hsv,red_low2,red_high2)

    mask_red=cv2.bitwise_or(mask_red1,mask_red2)

    # -------- VERDE --------
    green_low=np.array([40,40,40])
    green_high=np.array([80,255,255])
    mask_green=cv2.inRange(hsv,green_low,green_high)

    # -------- AZUL --------
    blue_low=np.array([100,150,0])
    blue_high=np.array([140,255,255])
    mask_blue=cv2.inRange(hsv,blue_low,blue_high)

    masks=[
        (mask_red,(0,0,255),"ROJO"),
        (mask_green,(0,255,0),"VERDE"),
        (mask_blue,(255,0,0),"AZUL")
    ]

    detected=False

    for mask,color,name in masks:

        kernel=np.ones((5,5),np.uint8)
        mask=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)

        contours,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        if len(contours)==0:
            continue

        cnt=max(contours,key=cv2.contourArea)

        area=cv2.contourArea(cnt)

        if area<4000:
            continue

        perimeter=cv2.arcLength(cnt,True)

        circularity = 4*math.pi*area/(perimeter*perimeter)

        approx=cv2.approxPolyDP(cnt,0.02*perimeter,True)

        x,y,w,h=cv2.boundingRect(cnt)

        shape=""

        if len(approx)==4:

            ratio=w/float(h)

            if 0.9<=ratio<=1.1:
                shape="Cuadrado"
            else:
                shape="Rectangulo"

        elif circularity>0.8:
            shape="Circulo"

        else:
            continue

        label=shape+" "+name

        cv2.rectangle(frame,(x,y),(x+w,y+h),color,3)
        cv2.putText(frame,label,(x,y-10),
        cv2.FONT_HERSHEY_SIMPLEX,0.8,color,2)

        print("Detectado:",label)

        if shape=="Circulo" and name=="ROJO":
            arduino.write(b'C')

        elif shape=="Rectangulo" and name=="VERDE":
            arduino.write(b'R')

        elif shape=="Cuadrado" and name=="AZUL":
            arduino.write(b'S')

        detected=True
        break

    if not detected:
        arduino.write(b'N')

    cv2.imshow("Deteccion forma y color",frame)

    if cv2.waitKey(1)==27:
        break

cam.release()
cv2.destroyAllWindows()