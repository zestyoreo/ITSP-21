#!/usr/bin/env python
import rospy
import random
import time
from std_msgs.msg import Header
from sensor_msgs.msg import JointState
from std_msgs.msg import Int32

class Arm_Control:

	def __init__(self):
		self.joint_positions = []
		self.num_interpolations = 100
		self.target_joint_positions = []
		self.position_steps = []
		self.joint_names = []
		self.typ = 0
		self.prev_state = [0,0,0,0,0,0,0,0,0,0]
		self.plate_positions = [[0,0,0,0,0,0,-1.56,0,0,0],[0,0,0,0,0,0,-1.56,0,-0.54,0.54],[0,0,0,0,0,0,-1.56,0,0,0]]
		#[["""position 1 of all 10 joints*"""]["""position 2 of all 10 joints*"""]["""position 3 of all 10 joints*"""]["""position 4 of all 10 joints*"""]] 
		self.plate_delays = [3,3,2]	#delay in seconds in each positions

		self.bowl_positions = [["""position 1 of all 10 joints*"""],["""position 2 of all 10 joints*"""],["""position 3 of all 10 joints*"""],["""position 4 of all 10 joints*"""]] 
		self.bowl_delays = [1,1,2]

		self.glass_positions = [["""position 1 of all 10 joints*"""],["""position 2 of all 10 joints*"""],["""position 3 of all 10 joints*"""],["""position 4 of all 10 joints*"""]] 
		self.glass_delays = [1,1,2]

		# Create ROS publisher
		self.data_publisher = rospy.Publisher('joint_states_interpolated', JointState, queue_size=10)

		# Give node name
		rospy.init_node('joint_state_interpolated_publisher')

		rospy.Subscriber("sequence_initiator", Int32, self.callback)

	def jointStatePublisher(self):

		# Set operation frequency
		self.rate = rospy.Rate(100) # 10hz

		# Create a robot joint state message
		self.robot_arm_joint_state = JointState()
		self.robot_arm_joint_state.header = Header()
		self.robot_arm_joint_state.header.stamp = rospy.Time.now()
		self.robot_arm_joint_state.name = self.joint_names
		self.robot_arm_joint_state.velocity = []
		self.robot_arm_joint_state.effort = []

		# Iitialise current step to 0
		self.current_interpolation = 0

		# Get type of utensil and execute sequence of movements accordingly

		if self.typ == 0:
			print("Stationery")
			self.robot_arm_joint_state.header.stamp = rospy.Time.now()
			self.robot_arm_joint_state.position = self.prev_state
			self.data_publisher.publish(self.robot_arm_joint_state)

		if self.typ==1:
			print ("Plate Sequence Initiated")
			self.exec_movements(self.plate_positions,self.plate_delays)
			self.typ==0
		elif self.typ==2:
			print ("Bowl Sequence Initiated")
			self.exec_movements(self.bowl_positions,self.bowl_delays)
			self.typ==0
		elif self.typ==3:
			print ("Glass Sequence Initiated")
			self.exec_movements(self.glass_positions,self.glass_delays)
			self.typ==0

	def callback(self,data):
		rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
		self.typ = int(data.data)
		
	def exec_movements(self,positions_list,delays):

		for i in range(len(positions_list)):

			#setting target positions for all joints
			self.target_joint_positions = positions_list[i]

			self.robot_arm_joint_state.header.stamp = rospy.Time.now()
			self.robot_arm_joint_state.position = self.target_joint_positions

			# publish robot joint state data to the topic
			self.data_publisher.publish(self.robot_arm_joint_state)
			self.prev_state = self.target_joint_positions
			self.rate.sleep()
			time.sleep(delays[i])

	def jointStatesCallback(self,msg):
		self.joint_names = msg.name
		temp_list = msg.position
		self.joint_positions = msg.position
		self.joint_velocities = msg.velocity
		self.joint_efforts = msg.effort


if __name__ == "__main__":
    try:
        arm = Arm_Control()

        # Create joint states' subscriber
        data_subscriber = rospy.Subscriber('joint_states', JointState, arm.jointStatesCallback)

        #Running Joint state Publisher
        while True:
        	arm.jointStatePublisher()

    except rospy.ROSInterruptException:
        pass