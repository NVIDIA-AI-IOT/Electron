import keras.caffe.convert as convert
import pprint
import argparse

"""

    USAGE EXAMPLE
        python caffe2keras.py -load_path 'models/' -prototxt 'train_val_for_keras.prototxt' -caffemodel 'bvlc_googlenet.caffemodel'

"""


def main():

    print("Converting model...")
    model = convert.caffe_to_keras('Networks/Other/train_val.prototxt', 'Networks/Other/snapshot_iter_117.caffemodel', 0)
    print("Finished converting model.")

    # Save converted model structure
    print("Storing model...")
    json_string = model.to_json()
    open(store_path + '/Keras_model_structure.json', 'w').write(json_string)
    # # Save converted model weights
    model.save_weights('Keras_model_weights.h5', overwrite=True)
    print("Finished storing the converted model to "+ store_path)


main()
