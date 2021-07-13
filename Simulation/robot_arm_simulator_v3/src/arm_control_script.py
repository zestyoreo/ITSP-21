#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def sequence_initiator():
    utensil_type = int(input("Enter the code of the sequence to be initiated (0,1,2). And enter 9 for shutdown."))
    pub = rospy.Publisher('sequence_initiator', Int32, queue_size=10)
    rospy.init_node('sequence_initiator_publisher')
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        utensil_type = int(input("Enter the code of the sequence to be initiated (0,1,2). And enter 9 for shutdown."))
        print(utensil_type)
        pub.publish(utensil_type)
        rate.sleep()

if __name__ == '__main__':
    try:
        sequence_initiator()
    except rospy.ROSInterruptException:
        pass
