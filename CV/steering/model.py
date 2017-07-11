"""
models.py

Functions to create and train Keras models plus a few common model Architectures.
I'd like to credit NVIDIA-Jetson/F1Epoch team for some of the stuff down here, they helped us a lot

"""
import keras
from keras.layers import Input, Dense, merge
from keras.models import Model
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D, SimpleRNN, Reshape, BatchNormalization
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.regularizers import l2
from keras.utils import plot_model
import helperFunctions


def get_model():
    lid = Input(shape = (360, ), name = 'lid')
    # x = Convolution2D(8, 2, 2)(lid)
    x = Activation('relu')(lid)
    # x = MaxPooling2D(pool_size=(2, 2))(x)

    # x = Convolution2D(16, 2, 2)(lid)
    x = Activation('relu')(lid)
    # x = MaxPooling2D(pool_size=(2, 2))(x)

    # x = Convolution2D(32, 2, 2)(lid)
    x = Activation('relu')(lid)
    # x = MaxPooling2D(pool_size=(2, 2))(x)

    # merged = Flatten()(x)

    x = Dense(128)(x)
    x = Activation('linear')(x)
    x = Dropout(.3)(x)

    jstk = Dense(1, name='jstk')(x)

    net = Model(input=[lid], output=[jstk])
    net.compile(optimizer='adadelta', loss='mean_squared_error')
    print(net.summary())
    return net

def trainModel(model, lidarIn, jstkOut):
    model.fit(x=lidarIn, y=jstkOut, batch_size=32, epochs=100, verbose=2, callbacks=None, validation_split=0.2, shuffle=True, initial_epoch=0)
    modelName = raw_input("Please enter the trained models filename")
    modelPng = modelName + ".png"
    modelName = modelName + ".h5"
    plot_model(model, to_file=modelPng)
    model.save(modelName)
    print("Saved as %s" %(modelName))
    return model

def testModel(model, testX, testY):
    # Test model and evauluate accuracy, prints it
    scores = model.evaluate(testX, testY)
    print("\nAccuracy: " + model.metrics_name[1], scores[1]*100)

unsplit_lidar, unsplit_joydata = helperFunctions.save_data_to_arrays('joyData.txt', 'scanData.txt')
train_lidar, val_lidar = helperFunctions.split_data_train_val(unsplit_lidar)
train_joy, val_joy = helperFunctions.split_data_train_val(unsplit_joydata)
lidModel = get_model()
trained_lidModel = trainModel(lidModel, train_lidar, train_joy)
testModel(trained_lidModel, val_lidar, val_joy)
