import os
import cv2
import numpy as np
from keras.models import model_from_json
from keras.preprocessing import image

#load model
model = model_from_json(open("fer.json", "r").read())
#load weights
model.load_weights('model_filter.h5')

face_haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


capture=cv2.VideoCapture(0)

while True:
    # captures frame and returns boolean value and captured image
    ret,frame=capture.read()
    if not ret:
        continue
    gray_img= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.32, 5)


    for (x,y,w,h) in faces_detected:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),thickness=2)
        #cropping region of interest i.e. face area from  image
        roi_gray=gray_img[y:y+w,x:x+h]
        roi_gray=cv2.resize(roi_gray,(48,48))
        img_pixels = image.img_to_array(roi_gray)
        img_pixels = np.expand_dims(img_pixels, axis = 0)
        img_pixels /= 255

        predictions = model.predict_emotion(img_pixels)

        #find max indexed array
        max_index = np.argmax(predictions[0])

        emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
        predicted_emotion = emotions[max_index]

        cv2.putText(frame, predicted_emotion, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    resized_img = cv2.resize(frame, (1000, 700))
    cv2.imshow('Facial emotion analysis ',resized_img)



    if cv2.waitKey(10) == ord('q'):#wait until 'q' key is pressed
        break

capture.release()
cv2.destroyAllWindows
