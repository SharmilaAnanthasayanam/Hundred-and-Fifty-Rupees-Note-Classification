# Hundred-and-Fifty-Rupees-Note-Classification

### Goal:
  To build an image classifier to classify Hundered and Fifty Rupees Indian Note using Tensorflow.

### Tools used:
* Tensorflow
* OpenCV
* Keras
* Numpy
* Matplotlib
* Streamlit

### Steps:
* Collected images using the Google Chrome Extension "Download All Images" and some by manually taking pictures.
* Preprocessing is done after collecting equal proportion of data for both classes.
    * Images with improper extensions are removed.
    * Images are loaded inside Keras utils library.
    * The values in images are scaled down to 0 to 255
* Data has been split into train, test and validation sets.
* Data resizing and scaling has been done and Augmented the data.
* HyperParameter Tuning has been done using Keras Tuner to arrive at best activation layer, Learning rate and Number of filters in each layer.
* Convolutional neural network contains sequentially placing convolution and max pooling layers. Finally flattened and dense layer is added followed by the output layer with single neuron. This neuron gives us value in the range of 0 to 1. We divide the classes by using threshold as 0.5.
* Once the model has been built and compiled, model is trained using the data.
* Number of epochs is decided by Early Stopping when val loss doesn't change for more than 3 epochs.
* Model is optimized using Adam Optimizer and loss is calculated using Binary Cross Entropy.
* Model has been validated using K-fold Cross validation and got 73% Accuracy.
* Applied data augmentation on the augmented data to increase dataset size. Trained the model and validated using Kfold Cross Validation. Accuracy has been increased to 86%.
* Saved the model and applied it to the Streamlit Web App.  

<img width="953" alt="image" src="https://github.com/SharmilaAnanthasayanam/Hundred-and-Fifty-Rupees-Note-Classification/assets/112562560/8ebd8cb5-3729-48a4-8acd-0c5b34b5233c">

<img width="955" alt="image" src="https://github.com/SharmilaAnanthasayanam/Hundred-and-Fifty-Rupees-Note-Classification/assets/112562560/2230b3e6-489f-485b-aa4f-d89d7f498bf7">





