import numpy as np
import matplotlib.pyplot as plt

import caffe

MODEL_FILE = 'Networks/InitialLegNet/deploy.prototxt'
PRETRAINED = 'Networks/InitialLegNet/snapshot_iter_117.caffemodel'
IMAGE_FILE = '0049.jpg'

caffe.set_mode_gpu()
net = caffe.Detector(MODEL_FILE, PRETRAINED,
                       mean=np.load('mean.npy').mean(1).mean(1),
                       channel_swap=(2,1,0),
                       raw_scale=255,
                       )#image_dims=(4032, 3024))
input_image = caffe.io.load_image(IMAGE_FILE)
out = net.forward()
print out
print out['bboxes'][0][0][0][0]
plt.show()
