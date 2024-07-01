#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class LimoController:
    def __init__(self):
        # Initialize the ROS node
        rospy.init_node('move_forward', anonymous=True)

        # Create a publisher to the cmd_vel topic
        self.vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        # Subscribe to the laser scan topic
        self.scan_sub = rospy.Subscriber('/scan', LaserScan, self.scan_callback)

        # Set the rate at which to send messages (10 Hz)
        self.rate = rospy.Rate(10)

        # Create a Twist message and set the initial linear velocity
        self.vel_msg = Twist()
        self.vel_msg.linear.x = 0.5  # Adjust this value to set the forward speed
        self.vel_msg.angular.z = 0.0

        # Variable to store whether an obstacle is detected
        self.obstacle_detected = False

        rospy.loginfo("Moving forward...")

    def scan_callback(self, data):
        # Check if there are any obstacles within 1 meter
        if min(data.ranges) < 1.0:
            self.obstacle_detected = True
        else:
            self.obstacle_detected = False

    def move_forward(self):
        # Publish the message indefinitely
        while not rospy.is_shutdown():
            if self.obstacle_detected:
                self.vel_msg.linear.x = 0.0  # Stop the robot
                rospy.loginfo("Obstacle detected! Stopping...")
            else:
                self.vel_msg.linear.x = 0.5  # Move forward

            self.vel_pub.publish(self.vel_msg)
            self.rate.sleep()

if __name__ == '__main__':
    try:
        controller = LimoController()
        controller.move_forward()
    except rospy.ROSInterruptException:
        pass

