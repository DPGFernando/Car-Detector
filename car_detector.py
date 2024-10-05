import cv2

cascade_path = 'C:/Users/Dinethra/Desktop/Programs/Python A.I/Car Detector/car_detectors.xml'
trained_car_data = cv2.CascadeClassifier(cascade_path)

img_path = 'C:/Users/Dinethra/Desktop/Programs/Python A.I/Car Detector/car.jpg'

img = cv2.imread(img_path)
#webcam = cv2.VideoCapture(0)
#car = cv2.VideoCapture('filename.mp4')

while True:

    #successful_frame_read, frame = webcam.read()
    grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    car_coordinates = trained_car_data.detectMultiScale(grayscaled_img)
    print(car_coordinates)
    
    for (x, y, w, h) in car_coordinates:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255, 0), 2)

    cv2.imshow('Clever Programmer Car Detector', img)
    key = cv2.waitKey(1)

    if key==81 or key==113:
        break
    
#webcam.release()

print ("Code Completed")