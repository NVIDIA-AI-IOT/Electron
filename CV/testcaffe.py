"""Loading a .caffemodel and figure out the encoding.
Author: Yuhuang Hu
Email : duguyue100@gmail.com
"""

from __future__ import absolute_import
from __future__ import print_function
import os
# from keras.utils.visualize_util import plot

from keras.datasets import mnist as dataset
from keras.utils import np_utils

import transcaffe as tc

batch_size = 128
nb_classes = 10
nb_epoch = 40

# input image dimensions
img_rows, img_cols = 28, 28
# number of convolutional filters to use
nb_filters = 32
# size of pooling area for max pooling
nb_pool = 2
# convolution kernel size
nb_conv = 3
# color channels
chnls = 1

# the data, shuffled and split between train and test sets



# define model for testing
data_path = os.environ["TRANSCAFFE_DATA"]

# model_str = os.path.join(data_path,
#                          "VGG_ILSVRC_16_layers_deploy.prototxt.txt")
model_str = os.path.join(data_path, "Networks/InitialLegNet/deploy.prototxt")
model_bin = os.path.join(data_path, "Networks/InitialLegNet/snapshot_iter_117.caffemodel")

model = tc.load(model_str, model_bin, target_lib="keras")

model.compile(loss='categorical_crossentropy', optimizer='adadelta',
              metrics=['accuracy'])
score = model.evaluate(X_test, Y_test, verbose=0)
print('Test score:', score[0])
print('Test accuracy:', score[1])
