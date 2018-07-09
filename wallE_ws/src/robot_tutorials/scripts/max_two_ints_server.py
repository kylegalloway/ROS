#! /usr/bin/env python
from robot_tutorials.srv import *
import rospy


def handle_max_two_ints(data):
    print("Returning max({}, {}) = {}".format(
        data.a, data.b, max(data.a, data.b)))
    return maxTwoIntsResponse(max(data.a, data.b))


def max_two_ints_server():
    rospy.init_node('max_two_ints_server')
    m = rospy.Service('max_two_ints', maxTwoInts, handle_max_two_ints)
    print("Ready to comppute max(a,b)")
    rospy.spin()


def main():
    max_two_ints_server()


if __name__ == '__main__':
    main()
