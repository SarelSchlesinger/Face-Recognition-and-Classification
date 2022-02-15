# ScoreFace

This program was written as part of JCT's Hackathon.
The app grades quality of facial images,
based on a neural network that was trained on a large data set of images divided into several categories.
The program gives the user feedback if the image was good, and if it ain't, what was the problem.
The neurons network training was performed using the Tensorflow library.

There are three files in the program:
model_training.py containing the code that was used to train the neural network.
main.py containing the code that receives an image from the user and returns output of the image quality.
Quality_analysis.py containing code that analyzes the raw output obtained from the model.
