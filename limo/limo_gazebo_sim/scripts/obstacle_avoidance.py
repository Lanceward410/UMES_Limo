#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class ObstacleAvoidance:
    def __init__(self):
        rospy.init_node('obstacle_avoidance', anonymous=True)
        
        # Publisher to control the robot's velocity
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        
        # Subscriber to the laser scan data
        self.laser_sub = rospy.Subscriber('/scan', LaserScan, self.laser_callback)
        
        # Variable to track if the robot should move forward
        self.move_forward = True
        
        rospy.spin()

    def laser_callback(self, data):
        # Check if there is an obstacle within 0.5 meters
        if min(data.ranges) < 0.5:
            self.move_forward = False
        else:
            self.move_forward = True

        # Publish the appropriate command
        self.publish_command()

    def publish_command(self):
        cmd = Twist()
        if self.move_forward:
            cmd.linear.x = 0.5  # Move forward with a velocity of 0.5 m/s
        else:
            cmd.linear.x = 0.0  # Stop
        self.cmd_vel_pub.publish(cmd)

if __name__ == '__main__':
    try:
        ObstacleAvoidance()
    except rospy.ROSInterruptException:
        pass

