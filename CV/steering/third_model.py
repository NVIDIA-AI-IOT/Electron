"""
models.py

Functions to create and train Keras models plus a few common model Architectures.
I'd like to credit NVIDIA-Jetson/F1Epoch team for some of the stuff down here, they helped us a lot

"""
import keras
from keras.layers import Input, Dense, merge
from keras.models import Model
from keras.models import Sequential
from keras.layers import Convolution2D, Convolution1D, MaxPooling2D, MaxPooling1D, SimpleRNN, Reshape, BatchNormalization
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.regularizers import l2
from keras.utils import plot_model
import helperFunctions


def get_model():
    # model = Sequential((
    #
    #     # Convolution1D(nb_filter=8, filter_length=2, activation='relu', input_shape=(360, )),
    #     MaxPooling1D(input_shape=(360, )),     # Downsample tfilter_lengthhe output of convolution by 2X.
    #     # Convolution1D(nb_filter=16, filter_length=2, activation='relu'),
    #     MaxPooling1D(),
    #     Flatten(),
    #     Dense(128, activation='linear'),
    #     Activation('relu'),
    #     Activation('relu'),
    #     Dropout(0.3),
    #     Dense(1, name='jstk'),
    #
    # ))
    lid = Input(shape = (360, 2), name = 'lid')
    x = Convolution1D(8, 2)(lid)
    x = Activation('relu')(x)
    x = MaxPooling1D(pool_size=(2))(x)

    x = Convolution1D(16, 2)(lid)
    x = Activation('relu')(x)
    x = MaxPooling1D(pool_size=(2))(x)

    x = Convolution1D(32, 2)(lid)
    x = Activation('relu')(x)
    x = MaxPooling1D(pool_size=(2))(x)

    x = Convolution1D(64, 2)(lid)
    x = Activation('relu')(x)
    x = MaxPooling1D(pool_size=(2))(x)

    x = Convolution1D(128, 2)(lid)
    x = Activation('relu')(x)
    x = MaxPooling1D(pool_size=(2))(x)

    x = Convolution1D(256, 2)(lid)
    x = Activation('relu')(x)
    x = MaxPooling1D(pool_size=(2))(x)

    x = Convolution1D(512, 2)(lid)
    x = Activation('relu')(x)
    x = MaxPooling1D(pool_size=(2))(x)

    x = Convolution1D(1024, 2)(lid)
    x = Activation('relu')(x)
    x = MaxPooling1D(pool_size=(2))(x)

    merged = Flatten()(x)

    x = Dense(128)(merged)
    x = Activation('linear')(x)
    x = Dropout(.3)(x)

    jstk = Dense(1, name='jstk')(x)

    net = Model(input=[lid], output=[jstk])
    net.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])
    print(net.summary())
    return net

def trainModel(model, lidarIn, jstkOut):
    model.fit(x=lidarIn, y=jstkOut, batch_size=32, epochs=250, verbose=2, callbacks=None, validation_split=0.2, shuffle=True, initial_epoch=0)
    modelName = raw_input("Please enter the trained models filename")
    modelPng = modelName + ".png"
    modelName = modelName + ".h5"
    plot_model(model, to_file=modelPng)
    model.save(modelName)
    print("Saved as %s" %(modelName))
    return model

unsplit_lidar, unsplit_joydata = helperFunctions.save_data_to_arrays('joyData.txt', 'scanData.txt')
lidModel = get_model()
trained_lidModel = trainModel(lidModel, unsplit_lidar, unsplit_joydata)
