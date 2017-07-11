import keras
from keras.layers import Input, Dense, merge
from keras.models import Model
from keras.models import Sequential
from keras.layers import Convolution2D, Convolution1D, MaxPooling2D, MaxPooling1D, SimpleRNN, Reshape, BatchNormalization
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.regularizers import l2
from keras.utils import plot_model
from keras.models import load_model

scanDataText = ''
model = load_model('actconv2d.h5')
stxt = scanDataText.split('\n')
lidarData = []
for line in stxt:
    line = line.replace('inf', 'None') # replace string so that I can use eval function
    if line.startswith('ranges'):
        edited = line[8:] # cuts the string so that it is left only with an array
        lidarData = eval(edited)
        break

count1 = 0
for y in lidarData:
    lidarData[count1] = [count1+1, y]
    count1 = count1 + 1

o = model.predict(np.array([resize]), batch_size=32, verbose=2)
output = o[0]
jstk = output[0]
