# ar_tag_filter.py
import rospy
from ar_track_alvar_msgs.msg import AlvarMarkers
from std_msgs.msg import Int32

def ar_pose_marker_callback(data):
    if data.markers:
        for marker in data.markers:
            if marker.id == 1:
                rospy.loginfo(f"Detected AR Tag ID: {marker.id}")
                pub.publish(marker.id)

rospy.init_node('ar_tag_filter')
pub = rospy.Publisher('/ar_tag', Int32, queue_size=10)
rospy.Subscriber('/chatter_updown', AlvarMarkers, ar_pose_marker_callback)
rospy.spin()

