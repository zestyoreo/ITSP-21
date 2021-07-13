#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
import cv2
import numpy as np
import tensorflow as tf
import time

def sequence_initiator(model):
  pub = rospy.Publisher('sequence_initiator', Int32, queue_size=10)
  rospy.init_node('sequence_initiator_publisher')
  rate = rospy.Rate(10) # 10hz

  cap = cv2.VideoCapture(0)
  t1 = time.time()
  time.sleep(2)
  utensil_type = 0
  while not rospy.is_shutdown():
    # Capture frame-by-frame
    ret, image= cap.read()

    # Display the resulting frame
    cv2.imshow('frame',image)
    t2 = time.time()
    if t2 - t1 >=10:
      # Image Preprocessing
      imgData = cv2.resize(image, (50,50))
      imgData=np.reshape(imgData,(1,50,50,3))
      # Prediction
      pred=model.predict(imgData)
      utensil_type=np.argmax(pred)
      print(utensil_type)
      t1 = time.time()
        
      ctrl_c = False
      while not ctrl_c:
        connections = pub.get_num_connections()
        if connections>0:
          pub.publish(utensil_type)
          print(utensil_type," is published")
          time.sleep(0.1)
          utensil_type = 0
          pub.publish(utensil_type)
          print(utensil_type," is published")
          ctrl_c = True
        else:    
          rate.sleep()

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break       

    # When everything done, release the capture
  cap.release()
  cv2.destroyAllWindows()

if __name__ == '__main__':
  try:
    model=tf.keras.models.load_model('/home/adi/ROS/rws/src/robot_arm_simulator/src/finalModel.h5')
    sequence_initiator(model)
  except rospy.ROSInterruptException:
    pass