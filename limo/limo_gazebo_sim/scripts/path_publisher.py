import rospy
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
'''
class PathPublisher:
    def __init__(self):
        rospy.init_node('path_publisher')
        self.path_pub = rospy.Publisher('/robot_path', Path, queue_size=10)
        self.path = Path()
        self.path.header.frame_id = 'odom'
        rospy.Subscriber('/odom', Odometry, self.odom_callback)
        rospy.spin()
'''
    def odom_callback(self, msg):
        pose = PoseStamped()
        pose.header = msg.header
        pose.pose = msg.pose.pose
        self.path.poses.append(pose)
        self.path.header.stamp = rospy.Time.now()
        self.path_pub.publish(self.path)

if __name__ == '__main__':
    rospy.init_node('path_publisher', anonymous=True)

    # Create a publisher for the /scan topic
    scan_publisher = rospy.Publisher('/robot_path', Path, queue_size=10)

    # Subscribe to the /limo/scan topic
    rospy.Subscriber('/odom', Odometry, odom_callback)

    # Keep the node running
    rospy.spin()

