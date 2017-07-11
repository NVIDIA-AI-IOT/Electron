"""
models.py

Functions to create and train Keras m(odels plus a few common model Architectures.

"""
import keras
from keras.layers import Input, Dense, merge
from keras.models import Model
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D, SimpleRNN, Reshape, BatchNormalization
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.regularizers import l2



def get_model():
    lid = Input(shape = (72, 2), name = 'lid')
    x = Convolution2D(8, 2, 2)(lid)
    x = Activation('relu')(x)
    x = MaxPooling2D(pool_size=(2, 2))(x)

    x = Convolution2D(16, 2, 2)(lid)
    x = Activation('relu')(x)
    x = MaxPooling2D(pool_size=(2, 2))(x)

    x = Convolution2D(32, 2, 2)(lid)
    x = Activation('relu')(x)
    x = MaxPooling2D(pool_size=(2, 2))(x)

    merged = Flatten()(x)

    x = Dense(128)(merged)
    x = Activation('linear')(x)
    x = Dropout(.3)(x)

    jstk = Dense(1, name='jstk')(x)

    net = Model(input=[lid], output=[jstk])
    net.compile(optimizer='adadelta', loss='mean_squared_error')
    print(net.summary())
    return net

def trainModel(model, lidarIn, jstkOut):
    #Trains predefined model with verbose logging, input image data and output steering data
    model.fit(x=imgIn, y=jstkOut, batch_size=32, epochs=100, verbose=2, callbacks=None, validation_split=0.2, shuffle=True, initial_epoch=0)
    modelName = raw_input("Please enter the trained models filename")
    modelPng = modelName + ".png"
    modelName = modelName + ".h5"
    #Plots the trained model
    plot_model(steerNet, to_file=modelPng)
    model.save(modelName)
    print("Saved as %s" %(modelName) )
    return model
