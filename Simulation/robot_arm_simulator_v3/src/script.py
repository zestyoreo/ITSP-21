#!/usr/bin/env python
import rospy
import random
from std_msgs.msg import Header
from sensor_msgs.msg import JointState

global JOINT_POSITIONS
JOINT_POSITIONS = []

NUM_INTERPOLATIONS = 100

global TARGET_JOINT_POSITIONS
TARGET_JOINT_POSITIONS = []

global POSITION_STEPS
POSITION_STEPS = []

global JOINT_NAMES
JOINT_NAMES = []

class Simim:

	def __init__(self):
    #POSITIONS FOR DIFFERENT SEQUENCES
		self.plate_positions = [[0.2819709311137173, -1.4543761821166057, 0.011850149430377543, -0.6983010354578446, 1.271919612769416, -1.4717381252723547, -0.9524538206233395, -0.6909746983104218, 0.7151183334970674, -0.42721390758044],[-0.01046557024441186, -0.7644569597877273, 0.7880557887830244, 1.2505332764290629, -0.8594482194748136, 1.323838686516399, -0.3396762701525362, 1.0749828061054603, 0.42190164742644964, 1.0933688871341591]]
		#[["""position 1 of all 10 joints*"""]["""position 2 of all 10 joints*"""]["""position 3 of all 10 joints*"""]["""position 4 of all 10 joints*"""]] 
		self.bowl_positions = [["""position 1 of all 10 joints*"""],["""position 2 of all 10 joints*"""],["""position 3 of all 10 joints*"""],["""position 4 of all 10 joints*"""]] 
		self.glass_positions = [["""position 1 of all 10 joints*"""],["""position 2 of all 10 joints*"""],["""position 3 of all 10 joints*"""],["""position 4 of all 10 joints*"""]] 

	def jointStatePublisher(self):
		# Create ROS publisher
		self.data_publisher = rospy.Publisher('joint_states_interpolated', JointState, queue_size=10)
		# Give node name
		rospy.init_node('joint_state_interpolated_publisher')
		# Set operation frequency
		self.rate = rospy.Rate(100) # 10hz

		# Create a robot joint state message
		self.robot_arm_joint_state = JointState()
		self.robot_arm_joint_state.header = Header()
		self.robot_arm_joint_state.header.stamp = rospy.Time.now()
		self.robot_arm_joint_state.name = JOINT_NAMES

		self.robot_arm_joint_state.velocity = []
		self.robot_arm_joint_state.effort = []

		self.current_interpolation = 0
		
		self.seq_var = 0 #got from integration with the CV system
		# Sequence of Movements
		if self.seq_var==0:
			self.exec_movements(self.plate_positions)
		elif self.seq_var==1:
		    self.exec_movements(self.bowl_positions)
		elif self.seq_var==2:
		    self.exec_movements(self.glass_positions)

	def pos_step(self):
		global TARGET_JOINT_POSITIONS
		global POSITION_STEPS
		global JOINT_POSITIONS
		if (len(JOINT_POSITIONS)) and (len(TARGET_JOINT_POSITIONS)):
		    POSITION_STEPS = [(target-current)/float (NUM_INTERPOLATIONS) for (target, current) in zip(TARGET_JOINT_POSITIONS, JOINT_POSITIONS)]
		
		print ("Current Joint Positions: %s" %(str(JOINT_POSITIONS)))
		print ("New Target joint positions: %s and steps: %s" %(str(TARGET_JOINT_POSITIONS), str(POSITION_STEPS)))

	def exec_movements(self,positions_list):
		global TARGET_JOINT_POSITIONS
		global POSITION_STEPS
		global JOINT_POSITIONS
		global NUM_INTERPOLATIONS

		i = 0
		TARGET_JOINT_POSITIONS = positions_list[i]
		self.pos_step()

		while not rospy.is_shutdown():

		    self.robot_arm_joint_state.header.stamp = rospy.Time.now()

		    if (self.current_interpolation < NUM_INTERPOLATIONS) and (len(POSITION_STEPS)):
		        self.current_interpolation += 1 
		        new_data = []
		        for index, data in enumerate(TARGET_JOINT_POSITIONS):
		            global POSITION_STEPS
		            new_data.append(JOINT_POSITIONS[index] + POSITION_STEPS[index])
		        self.robot_arm_joint_state.position = new_data

		        # Publish robot joint state data to the topic
		        self.data_publisher.publish(self.robot_arm_joint_state)
		        self.rate.sleep()

		    if (self.current_interpolation == NUM_INTERPOLATIONS - 1):
		        self.current_interpolation = 0
			
			if i>=(len(positions_list)-1) and (self.current_interpolation == NUM_INTERPOLATIONS - 1):break

		    elif i<(len(positions_list)-1) and (self.current_interpolation == NUM_INTERPOLATIONS - 1):
		        	i += 1
		        	TARGET_JOINT_POSITIONS = positions_list[i]
		        	self.pos_step()	

def jointStatesCallback(msg):
	global JOINT_NAMES
	JOINT_NAMES = msg.name

	temp_list = msg.position

	global JOINT_POSITIONS
	JOINT_POSITIONS = msg.position

	global JOINT_VELOCITIES
	JOINT_VELOCITIES = msg.velocity
	global JOINT_EFFORTS
	JOINT_EFFORTS = msg.effort

if __name__ == "__main__":
    try:
        inst = Simim()
        # Create joint states' subscriber
        data_subscriber = rospy.Subscriber('joint_states', JointState, jointStatesCallback)
        inst.jointStatePublisher()
    except rospy.ROSInterruptException:
        pass
