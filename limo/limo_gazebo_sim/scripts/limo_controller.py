# limo_controller.py
import rospy
from std_msgs.msg import Int32
from geometry_msgs.msg import Twist

def ar_tag_callback(data):
    if data.data == 1:
        rospy.loginfo("AR Tag ID 1 detected. Stopping the robot.")
        stop_robot()

def stop_robot():
    stop_msg = Twist()
    stop_msg.linear.x = 0
    stop_msg.angular.z = 0
    pub.publish(stop_msg)

rospy.init_node('limo_controller')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
rospy.Subscriber('/chatter_updown', Int32, ar_tag_callback)
rospy.spin()

