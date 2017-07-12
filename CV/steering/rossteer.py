#!/usr/bin/env python
import keras
import rospy
import numpy as np
#from keras.layers import Input, Dense, merge
#from keras.models import Model
#from keras.layers import Convolution2D, Convolution1D, MaxPooling2D, MaxPooling1D, SimpleRNN, Reshape, BatchNormalization
#from keras.layers import Activation, Dropout, Flatten, Dense
#from keras.regularizers import l2
#from keras.utils import plot_model
from keras.models import load_model
from std_msgs.msg import String

def callback(data):
    tempStr = str(data)
    tempStr = tempStr.replace("inf", 'None')
    tempStr = tempStr.replace("data: (", "[")
    tempStr = tempStr.replace(")", "]")

    #scanDataText = ''
    model = load_model('actconv2d.h5')

    """
    stxt = scanDataText.split('\n')
    lidarData = []
    for line in stxt:
        line = line.replace('inf', 'None') # replace string so that I can use eval function
        if line.startswith('ranges'):
            edited = line[8:] # cuts the string so that it is left only with an array
            lidarData = eval(edited)
            break
    """

    lidarData = eval(tempStr)


    count1 = 0
    for y in lidarData:
        lidarData[count1] = [count1+1, y]
        count1 = count1 + 1
    
    lidarData = [lidarData]
    #print(lidarData)

    o = model.predict(np.array(lidarData), batch_size=32, verbose=2)
    output = o[0]

    print (o)

    jstk = output[0]
    print(jstk)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/strScan", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
