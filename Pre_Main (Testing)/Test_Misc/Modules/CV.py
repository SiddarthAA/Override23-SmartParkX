import cv2
from GNP import Get_Number_Plate


def Final():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Camera Frame")
    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed To Open Camera")
            break 
        cv2.imshow("Number Plate Capture", frame)

        k = cv2.waitKey(1)
        if k%256 == 27: 
            print("\n--Closing Camera--")
            break 

        if k%256 == 32:
            imgname = "VehicleNumber.jpg"
            cv2.imwrite(imgname, frame)
            print(Get_Number_Plate(imgname))

Final()