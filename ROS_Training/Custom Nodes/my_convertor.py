#!/usr/bin/env python
# license removed for brevity
import rospy
import math
from beginner_tutorial.msg import quaternions
from beginner_tutorial.msg import euler_angles

class q_and_e:

	def __init__(self):

		rospy.init_node('my_convertor', anonymous=True)
	    self.conv_sub = rospy.Subscriber('topic1', quaternions, self.euler_conv)
		self.conv_pub = rospy.Publisher('topic2', euler_angles, queue_size=10)
	    
	    self.rate = rospy.Rate(10)

	    self.quat=quaternions()
	    self.eul = euler_angles()

	def euler_conv(self, data):
		self.quat = data

	    #roll (x-axis rotation)
	    sinr_cosp = 2 * (self.quat.w * self.quat.x + self.quat.y * self.quat.z)
	    cosr_cosp = 1 - 2 * (self.quat.x * self.quat.x + self.quat.y * self.quat.y)
	    self.eul.roll = atan2(sinr_cosp, cosr_cosp)

	    #pitch (y-axis rotation)
	    sinp = 2 * (self.quat.w * self.quat.y - self.quat.z * self.quat.x)
	    if fabs(sinp) >= 1:
	        self.eul.pitch = copysign(3.14159/ 2, sinp) #use 90 degrees if out of range
	    else:
	        self.eul.pitch = asin(sinp);

	    #yaw (z-axis rotation)
	    siny_cosp = 2 * (self.quat.w * self.quat.z + self.quat.x * self.quat.y)
	    cosy_cosp = 1 - 2 * (self.quat.y * self.quat.y + self.quat.z * self.quat.z)
	    self.eul.yaw = atan2(siny_cosp, cosy_cosp)

	def run(self):
		self.conv_pub.publish(self.eul)    
	    rospy.spin()

if __name__ == '__main__':
	try:
        x=q_and_e()
        x.run()
    except rospy.ROSInterruptException:
        pass