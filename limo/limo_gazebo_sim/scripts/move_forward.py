#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def move_forward():
    # Initialize the ROS node
    rospy.init_node('move_forward', anonymous=True)

    # Create a publisher to the cmd_vel topic
    vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    # Set the rate at which to send messages (10 Hz)
    rate = rospy.Rate(10)

    # Create a Twist message and set the linear velocity
    vel_msg = Twist()
    vel_msg.linear.x = 0.5  # Adjust this value to set the forward speed
    vel_msg.angular.z = 0.0

    rospy.loginfo("Moving forward...")

    # Publish the message indefinitely
    while not rospy.is_shutdown():
        vel_pub.publish(vel_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        move_forward()
    except rospy.ROSInterruptException:
        pass

