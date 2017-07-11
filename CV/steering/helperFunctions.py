import numpy as np

SPLIT_STRING = '---'

def get_lidar_avg_data_list(data_list):
    out = list() # output list
    high = 5 # average every 5 angles to use as 1 reading
    temp = list() # temporary list used to save values to average later
    for tup in data_list:
        if tup[1] <= high: # check if reading angle is in the range of 5
            temp.append(tup[2]) # add the distance to the temp list to average later
        else: # if the reading is in a new set of 5 readings
            out.append([high-5, sum(temp)/len(temp)])
            high = high + 5
            temp = list()
            temp.append(tup[2])
    return out

def formatt(joyDataTxt, scanDataTxt):
    jtxt = open(joyDataTxt, 'r') # open joystick data
    stxt = open(scanDataTxt, 'r') # open lidar data

    lidarTimeStamps = []
    lidarData = []
    joyStickTimeStampsTemp = []
    joystickDataTemp = []

    count = 0
    tempSec = 0
    tempNSec = 0
    for line in stxt:
        line = line.replace('inf', 'None') # replace string so that I can use eval function
        if line.startswith('ranges'):
            edited = line[8:] # cuts the string so that it is left only with an array
            lidarData.append(eval(edited)) # parse the array string of lidar data to an array and add that array to a list
        if line.startswith('    secs'):
            edited = line[10:]
            tempSec = eval(edited) # parse the seconds number
        if line.startswith('    nsecs'):
            edited = line[11:]
            tempNSec = eval(edited) # parse the nsecs number
            lidarTimeStamps.append((tempSec*1000)+(tempNSec/1000000)) # create timestamp and add that to list
        count = count + 1

    # read comments of above loop to see how this works. It's pretty much the same except for joystick
    for line in jtxt:
        line = line.replace('inf', 'None')
        if line.startswith('axes'):
            edited = line[6:]
            joystickDataTemp.append(eval(edited))
        if line.startswith('    secs'):
            edited = line[10:]
            tempSec = eval(edited)
        if line.startswith('    nsecs'):
            edited = line[11:]
            tempNSec = eval(edited)
            joyStickTimeStampsTemp.append((tempSec*1000)+(tempNSec/1000000))
        count = count + 1

    joystickData = []
    for lidStamp in lidarTimeStamps:
        closest = min(joyStickTimeStampsTemp, key=lambda x: abs(x-long(lidStamp))) # find closest joystick value to lidar value via timestamp
        num = 0
        for j in joyStickTimeStampsTemp:
            if j == closest:
                joystickData.append(joystickDataTemp[num]) # get the joy data based on timestamp and add that to real joydata output
                break
            num = num + 1
    return lidarData, joystickData

lid, joys = formatt('joyData.txt', 'scanData.txt')
print(len(lid))
print(len(joys))
