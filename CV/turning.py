import numpy as np
import cv2
import math

ANGLE_OF_VISION = 1.36136
camera = cv2.VideoCapture(0)

def get_point_distance(x, y, x1, y1):
    return math.sqrt(((x-x1)**2) + ((y-y1)**2))

def get_angle_of_foot(oframe, leg_point):
    width, height, channels = oframe.shape
    center_pixel_point = [width/2, height/2]
    triangle_base_length = get_point_distance(leg_point[0], leg_point[1], center_pixel_point[0], center_pixel_point[1])
    triangle_base_height = triangle_base_length/math.tan(ANGLE_OF_VISION/2)
    return math.atan(triangle_base_length / triangle_base_height)

file_read = open("test.txt", "r")
line_num = 0;
len_file = len(file_read.readlines())
while True:
    file_read = open("test.txt", "r")
    lines = file_read.readlines()
    if len_file is not len(file_read.readlines()):
        print lines
        while not lines[line_num][0].isdigit():
            line_num = line_num + 1
        splits = lines[line_num].split()
        leg_left_point = [splits[0], splits[1]] #this is temporary until we get ros up and running
        leg_right_point = [splits[2], splits[3]] #this is temporary until we get ros up and running
        print leg_left_point
        grabbed, frame = camera.read()
        frame = cv2.flip(frame, 1)

        print "angle range between which leg exists: " , get_angle_of_foot(frame, leg_left_point), " to ", get_angle_of_foot(frame, leg_right_point)
        line_num = line_num+1
        len_file = len(file_read.readlines())
