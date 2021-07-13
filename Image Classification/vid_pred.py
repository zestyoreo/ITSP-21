#!/usr/bin/env python
import cv2
import numpy as np
import tensorflow as tf

model=tf.keras.models.load_model('finalModel.h5')
cap = cv2.VideoCapture(0)

while(True):
  # Capture frame-by-frame
  ret, image= cap.read()

  # Display the resulting frame
  cv2.imshow('frame',image)
  # Image Preprocessing
  imgData = cv2.resize(image, (50,50))
  imgData=np.reshape(imgData,(1,50,50,3))
  # Prediction
  pred=model.predict(imgData)
  utensil_type=np.argmax(pred)
  print(utensil_type)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
