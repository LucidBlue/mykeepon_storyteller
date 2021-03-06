#! /usr/bin/env python

import roslib; roslib.load_manifest('mykeepon_storyteller')
import rospy
from mykeepon_storyteller.msg import ControllerMsg
from mykeepon_storyteller.msg import AudioMsg
from time import sleep
import sys

from states_and_actions import *

def main():
	global ino_pub#, launchID
	
	#launchID = int(sys.argv[1])
	
	# Initialize ROS node
	rospy.init_node('controller')
	
	# Create publisher to send out ControllerMsg messages
	ino_pub = rospy.Publisher('controller_data', ControllerMsg)
	
	# Subscribe to the audio data stream
	rospy.Subscriber('audio_data', ControllerMsg, audio_callback2, queue_size=1)
	
	rospy.loginfo("Controller node inititalized.")
	
	# Allow the program to listen without blocking
	rospy.spin()

def audio_callback2(data):
	pan 	= data.pan
	tilt 	= data.tilt
	roll 	= data.roll
	bop = data.bop
	controller_msg = ControllerMsg()
	#print(current_pos)

	controller_msg.ID = 0
	controller_msg.pan = pan
	controller_msg.tilt = tilt
	controller_msg.roll = roll
	controller_msg.bop = bop
	rospy.loginfo('sending: pan='+str(pan)+' tilt='+str(tilt)+' roll='+str(roll) + ' bop='+str(bop))
	ino_pub.publish(controller_msg)

def audio_callback(data):
	valence 	= data.valence
	intensity 	= data.intensity
	action 		= data.action
	
	controller_msg = ControllerMsg()
	#print(current_pos)

	pan,tilt,roll,bop = action_list[action](valence_list[valence], intensity_list[intensity])
	controller_msg.ID = 0
	controller_msg.pan = pan
	controller_msg.tilt = tilt
	controller_msg.roll = roll
	controller_msg.bop = bop
	rospy.loginfo('sending: pan='+str(pan)+' tilt='+str(tilt)+' roll='+str(roll) + ' bop='+str(bop))
	ino_pub.publish(controller_msg)
	
	"""
	pan,tilt,roll,bop = goto_resting(valence_list[valence], intensity_list[intensity])
	controller_msg.ID = 0
	controller_msg.pan = pan
	controller_msg.tilt = tilt
	controller_msg.roll = roll
	rospy.loginfo('sending: pan='+str(pan)+' tilt='+str(tilt)+' roll='+str(roll) + ' bop='+str(bop))
	ino_pub.publish(controller_msg)
	"""
	
# more complex actions, formed of primitives from states_and_actions

"""
def look_around(valence, intensity):
	controller_msg = ControllerMsg()
	
	saa.goto_resting()
	position = saa.lookleft(valence, intensity)
	pan,tilt,roll,bop = position
	controller_msg.ID = 0
	controller_msg.pan = pan
	controller_msg.tilt = tilt
	controller_msg.roll = roll
	rospy.loginfo('sending: pan='+str(pan)+' tilt='+str(tilt)+' roll='+str(roll))
	ino_pub.publish(controller_msg)
	sleep(0.1)

	position = saa.goto_resting()
	pan,tilt,roll,bop = position
	controller_msg.ID = 0
	controller_msg.pan = pan
	controller_msg.tilt = tilt
	controller_msg.roll = roll
	rospy.loginfo('sending: pan='+str(pan)+' tilt='+str(tilt)+' roll='+str(roll))
	ino_pub.publish(controller_msg)
	sleep(0.1)

	position = saa.lookleft(valence, intensity)
	pan,tilt,roll,bop = position
	controller_msg.ID = 0
	controller_msg.pan = pan
	controller_msg.tilt = tilt
	controller_msg.roll = roll
	rospy.loginfo('sending: pan='+str(pan)+' tilt='+str(tilt)+' roll='+str(roll))
	ino_pub.publish(controller_msg)


def walk_step(valence, intensity):
	controller_msg = ControllerMsg()
	saa.goto_resting(valence,intensity)
	position = saa.bopup(valence,intensity)
	pan,tilt,roll,bop = position
	controller_msg.ID = 0
	controller_msg.pan = pan
	controller_msg.tilt = tilt
	controller_msg.roll = roll
	rospy.loginfo('sending: pan='+str(pan)+' tilt='+str(tilt)+' roll='+str(roll))
	ino_pub.publish(controller_msg)
"""

if __name__ == '__main__':
	main()




