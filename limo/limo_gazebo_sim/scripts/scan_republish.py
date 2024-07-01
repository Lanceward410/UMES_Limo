#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def scan_callback(data):
    # Republish the data to the /scan topic
    scan_publisher.publish(data)

if __name__ == '__main__':
    rospy.init_node('scan_republisher', anonymous=True)

    # Create a publisher for the /scan topic
    scan_publisher = rospy.Publisher('/scan', LaserScan, queue_size=10)

    # Subscribe to the /limo/scan topic
    rospy.Subscriber('/limo/scan', LaserScan, scan_callback)

    # Keep the node running
    rospy.spin()

