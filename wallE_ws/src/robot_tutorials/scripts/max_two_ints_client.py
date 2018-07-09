#! /usr/bin/env python
import sys
import rospy
from robot_tutorials.srv import *


def max_two_ints_client(x, y):
    rospy.wait_for_service('max_two_ints')
    try:
        max_two_ints = rospy.ServiceProxy('max_two_ints', maxTwoInts)
        resp = max_two_ints(x, y)
        return resp.max
    except rospy.ServiceException, e:
        print("Service call failed: {}".format(e))


def usage():
    return "{} [{} {}]".format(sys.argv[0], a, b)


def main():
    if(len(sys.argv) == 3):
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print usage()
        sys.exit(1)
    print("Requesting max({} {})".format(x, y))
    print("max({}, {}) = {}".format(x, y, max_two_ints_client(x, y)))


if __name__ == '__main__':
    main()
