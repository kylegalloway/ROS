#! /usr/bin/env python
import rospy
from std_msgs.msg import String, Int8


def wallE_talker():
    hello_pub = rospy.Publisher('hello', String, queue_size=10)
    hello_pub_int = rospy.Publisher('hello_int', Int8, queue_size=10)
    rospy.init_node('wallE', anonymous=True)
    rate = rospy.Rate(10)
    counter = 0
    while not rospy.is_shutdown():
        greeting = "Hello, Eva!"
        greeting_int = ord(greeting[counter % len(greeting)])
        rospy.loginfo(greeting)
        hello_pub.publish(greeting)
        hello_pub_int.publish(greeting_int)
        counter += 1
        rate.sleep()


def main():
    try:
        wallE_talker()
    except rospy.ROSInterruptException:
        pass


if __name__ == '__main__':
    main()
