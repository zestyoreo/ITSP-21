#!/usr/bin/env python
import rospy
import random
import time
from std_msgs.msg import Header
from sensor_msgs.msg import JointState


class Arm_Control:

	def __init__(self):
		self.joint_positions = []
		self.num_interpolations = 100
		self.target_joint_positions = []
		self.position_steps = []
		self.joint_names = []

		self.plate_positions = [[0, 0, 0, 0, 0, 0, -1.56, 0, 0, 0], [0, 0, 0,
		    0, 0, 0, -1.56, 0, -0.54, 0.54], [0, 0, 0, 0, 0, 0, -1.56, 0, 0, 0]]
		# [["""position 1 of all 10 joints*"""]["""position 2 of all 10 joints*"""]["""position 3 of all 10 joints*"""]["""position 4 of all 10 joints*"""]]
		self.plate_delays = [3, 3, 2]  # delay in seconds in each positions

		self.bowl_positions = [["""position 1 of all 10 joints*"""], ["""position 2 of all 10 joints*"""],
		    ["""position 3 of all 10 joints*"""], ["""position 4 of all 10 joints*"""]]
		self.bowl_delays = [1, 1, 2]

		self.glass_positions = [["""position 1 of all 10 joints*"""], ["""position 2 of all 10 joints*"""],
		    ["""position 3 of all 10 joints*"""], ["""position 4 of all 10 joints*"""]]
		self.glass_delays = [1, 1, 2]

	def jointStatePublisher(self):

		# Create ROS publisher
		self.data_publisher = rospy.Publisher(
		    'joint_states_interpolated', JointState, queue_size=10)

		# Give node name
		rospy.init_node('joint_state_interpolated_publisher')

		# Set operation frequency
		self.rate = rospy.Rate(100)  # 10hz

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
		typ = int(input("Enter Sequence to be initiated."))
		if typ == 0:
			print("Plate Sequence Initiated")
			self.exec_movements(self.plate_positions, self.plate_delays)
			typ == None
		elif typ == 1:
			print("Bowl Sequence Initiated")
			self.exec_movements(self.bowl_positions, self.bowl_delays)
			typ == None
		else:
			print("Glass Sequence Initiated")
			self.exec_movements(self.glass_positions, self.glass_delays)
			typ == None

	def exec_movements(self, positions_list, delays):

		for i in range(len(positions_list)):

			# setting target positions for all joints
			self.target_joint_positions = positions_list[i]
			self.pos_to_step()

			for j in range(self.num_interpolations+2):
				self.robot_arm_joint_state.header.stamp = rospy.Time.now()

				if ((self.current_interpolation < self.num_interpolations) and (len(self.position_steps))):
					self.current_interpolation += 1
			        new_data = []
			        for index, data in enumerate(self.target_joint_positions):
			            new_data.append(
			                self.joint_positions[index] + self.position_steps[index])
			        self.robot_arm_joint_state.position = new_data

			        # publish robot joint state data to the topic
			        self.data_publisher.publish(self.robot_arm_joint_state)
			        self.rate.sleep()
					
				if (self.current_interpolation >= self.num_interpolations):
					self.current_interpolation = 0
			    	time.sleep(delays[i])
			    	break

	def pos_to_step(self):	#split the single step into multiple steps to acheive target

		if (len(self.joint_positions)) and (len(self.target_joint_positions)):
		    self.position_steps = [(target-current)/float (self.num_interpolations) for (target,current) in zip(self.target_joint_positions, self.joint_positions)]
		
		print ("current joint positions: %s" %(str(self.joint_positions)))
		print ("new target joint positions: %s a nd steps: %s" %(str(self.target_joint_positions), str(self.position_steps)))

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

        # Running Joint state Publisher
        while True:
        	arm.jointStatePublisher()

    except rospy.ROSInterruptException:
        pass
