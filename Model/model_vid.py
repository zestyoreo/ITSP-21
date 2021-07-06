#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
import cv2
import numpy as np
import tensorflow as tf

def sequence_initiator(model):
  pub = rospy.Publisher('sequence_initiator', Int32, queue_size=10)
  rospy.init_node('sequence_initiator_publisher')
  rate = rospy.Rate(10) # 10hz
  
  while not rospy.is_shutdown():
    cap = cv2.VideoCapture(0)
    while not rospy.is_shutdown():
      # Capture frame-by-frame
      ret, image= cap.read()

      # Display the resulting frame
      cv2.imshow('frame',image)
      imgData = cv2.resize(image, (50,50))
      imgData=np.reshape(imgData,(1,50,50,3))

      pred=model.predict(imgData)
      utensil_type=np.argmax(pred)
      print(utensil_type)
      print(rospy.get_time())
        
      ctrl_c = False
          
      while not ctrl_c:
        connections = pub.get_num_connections()
        if connections>0:
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
    model=tf.keras.models.load_model('finalModel.h5')
    sequence_initiator(model)
  except rospy.ROSInterruptException:
    pass