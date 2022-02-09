import numpy as np
import tensorflow as tf
import cv2
from CutPic import *
from Quality_Analysis import *


modelPath = "model2.tflite"
interpreter = tf.lite.Interpreter(modelPath)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


def process(image):
    shape_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_data = cv2.resize(shape_image, (300, 300))
    image_data = image_data[np.newaxis, ...].astype(np.uint8)
    return image_data

def imageProcessing(imagePath):
    new_image = CutPic(imagePath)
    image = cv2.imread(new_image)
    input_data = process(image)
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()

    output_data = interpreter.get_tensor(output_details[0]['index'])

    predictions = np.squeeze(output_data)
    p_scale, p_mean = output_details[0]['quantization']
    predictions = (predictions - p_mean * 1.0) * p_scale
    predictions_list = list(predictions)
    output_dict = dict()
    labels = ['blur', 'dark', 'mask', 'good', 'pose', 'rotate', 'sunglasses']
    for index, value in enumerate(predictions_list):
        output_dict[labels[index]] = value*100

    print(output_dict)

    return Quality_Analysis(output_dict)

print(imageProcessing(r"C:\Users\User\Pictures\Camera Roll\WIN_20220209_20_58_06_Pro.jpg"))