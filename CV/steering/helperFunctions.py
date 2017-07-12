import numpy as np

def save_data_to_arrays(joyDataTxt, scanDataTxt):
    jtxt = open(joyDataTxt, 'r') # open joystick data
    stxt = open(scanDataTxt, 'r') # open lidar data

    lidarTimeStamps = [] # this is the list containing the timestamps of the lidar data
    lidarData = [] # this is the lidar data put in the same order as the list above so they correlate with each other
    joyStickTimeStampsTemp = [] # this is a list of joystick timestamps which can be used to map joystick data to lidar data
    joystickDataTemp = [] # this is unfiltered joystick data that can be mapped to lidar data as a label to the input of the lidar
    joystickData = [] # joy data that has been mapped to lidar data

    tempSec = 0 # this number is updated every time the program hits a seconds tag in the data text file
    tempNSec = 0 # same as above but for nanoseconds
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

    # if not understood above, eval is able to take in a text representation of a number, array, or whatever type and can convert that
    # into manipulatable data

    # read comments of above loop to see how this works. It's pretty much the same except for joystick
    for line in jtxt:
        line = line.replace('inf', 'None') # did this so that I could use eval later
        if line.startswith('axes'):
            edited = line[6:]
            joystickDataTemp.append(eval(edited)[3])
        if line.startswith('    secs'):
            edited = line[10:]
            tempSec = eval(edited)
        if line.startswith('    nsecs'):
            edited = line[11:]
            tempNSec = eval(edited)
            joyStickTimeStampsTemp.append((tempSec*1000)+(tempNSec/1000000))

    for lidStamp in lidarTimeStamps:
        closest = min(joyStickTimeStampsTemp, key=lambda x: abs(x-long(lidStamp))) # find closest joystick value to lidar value via timestamp
        num = 0
        for j in joyStickTimeStampsTemp:
            if j == closest:
                joystickData.append(joystickDataTemp[num]) # get the joy data based on timestamp and add that to real joydata output
                break
            num = num + 1
    count = 0
    for x in lidarData:
        count1 = 0
        for y in lidarData[count]:
            lidarData[count][count1] = [count1+1, y]
            count1 = count1 + 1
        count1 = 0
        count = count + 1

    for i in xrange(len(joystickData)):
        print(str(joystickData[i]))
    return np.array(lidarData), np.array(joystickData)

# ld, jd = save_data_to_arrays('joyData.txt', 'scanData.txt')
# print(ld)
# print(ld[0])
# print(len(ld[0]))
# print(len(ld))
# print(ld.shape)
# print(jd.shape)
