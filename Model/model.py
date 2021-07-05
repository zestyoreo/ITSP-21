import cv2
import numpy as np
import tensorflow as tf

image=cv2.imread('image.jpeg')
imgData = cv2.resize(image, (50,50))
model=tf.keras.models.load_model('finalModel.h5')
imgData=np.reshape(imgData,(1,50,50,3))
pred=model.predict(imgData)
clas=np.argmax(pred)
print(clas)