#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time
#from turtlesim.msg import Pose
#from math import pow, atan2, sqrt
def talker():
    vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('my_initials', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    
    vel_msg=Twist()
    f=2
    l=0.78

    time.sleep(2*f)

    if not rospy.is_shutdown():
        vel_msg.linear.x=2
        vel_msg.linear.y=0
        vel_msg.linear.z=0

        vel_msg.angular.x=0
        vel_msg.angular.y=0
        vel_msg.angular.z=0
        vel_pub.publish(vel_msg)
        time.sleep(f)


        vel_msg.linear.x=0
        vel_msg.linear.y=0
        vel_msg.linear.z=0

        vel_msg.angular.x=0
        vel_msg.angular.y=0
        vel_msg.angular.z=2
        vel_pub.publish(vel_msg)
        time.sleep(l)


        vel_msg.linear.x=2
        vel_msg.linear.y=0
        vel_msg.linear.z=0

        vel_msg.angular.x=0
        vel_msg.angular.y=0
        vel_msg.angular.z=0
        vel_pub.publish(vel_msg)
        time.sleep(f)


        vel_msg.linear.x=0
        vel_msg.linear.y=0
        vel_msg.linear.z=0

        vel_msg.angular.x=0
        vel_msg.angular.y=0
        vel_msg.angular.z=2
        vel_pub.publish(vel_msg)
        time.sleep(l)


        vel_msg.linear.x=2
        vel_msg.linear.y=0
        vel_msg.linear.z=0

        vel_msg.angular.x=0
        vel_msg.angular.y=0
        vel_msg.angular.z=0
        vel_pub.publish(vel_msg)
        time.sleep(f)


        vel_msg.linear.x=0
        vel_msg.linear.y=0
        vel_msg.linear.z=0

        vel_msg.angular.x=0
        vel_msg.angular.y=0
        vel_msg.angular.z=2
        vel_pub.publish(vel_msg)
        time.sleep(l)  


        vel_msg.linear.x=2
        vel_msg.linear.y=0
        vel_msg.linear.z=0

        vel_msg.angular.x=0
        vel_msg.angular.y=0
        vel_msg.angular.z=0
        vel_pub.publish(vel_msg)
        time.sleep(f)
        vel_msg.linear.x=2
        vel_msg.linear.y=0
        vel_msg.linear.z=0

        vel_msg.angular.x=0
        vel_msg.angular.y=0
        vel_msg.angular.z=0
        vel_pub.publish(vel_msg)
        time.sleep(f)


        vel_msg.linear.x=0
        vel_msg.linear.y=0
        vel_msg.linear.z=0

        vel_msg.angular.x=0
        vel_msg.angular.y=0
        vel_msg.angular.z=2
        vel_pub.publish(vel_msg)
        time.sleep(l) 


        vel_msg.linear.x=2
        vel_msg.linear.y=0
        vel_msg.linear.z=0

        vel_msg.angular.x=0
        vel_msg.angular.y=0
        vel_msg.angular.z=0
        vel_pub.publish(vel_msg)
        time.sleep(f)

        vel_msg.linear.x=0
        vel_msg.linear.y=0
        vel_msg.linear.z=0

        vel_msg.angular.x=0
        vel_msg.angular.y=0
        vel_msg.angular.z=2
        vel_pub.publish(vel_msg)
        time.sleep(l) 


        vel_msg.linear.x=2
        vel_msg.linear.y=0
        vel_msg.linear.z=0

        vel_msg.angular.x=0
        vel_msg.angular.y=0
        vel_msg.angular.z=0
        vel_pub.publish(vel_msg)
        time.sleep(f)


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass