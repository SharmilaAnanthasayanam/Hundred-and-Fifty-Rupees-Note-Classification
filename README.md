# Hundred-and-Fifty-Rupees-Note-Classification

### Goal:
  To build an image classifier to classify Hundered and Fifty Rupees Indian Note using Tensorflow.

### Tools used:
* Tensorflow
* OpenCV
* Keras
* Numpy
* Matplotlib

### Steps:
* Collected images using the Google Chrome Extension "Download All Images" and some by manually taking pictures.
* Preprocessing is done after collecting equal proportion of data for both classes.
    * Images with improper extensions are removed.
    * Images are loaded inside Keras utils library.
    * The values in images are scaled down to 0 to 255
* Data has been split into train, test and validation sets.
* Convolutional neural network has been built by sequentially placing convolution and max pooling layers. Finally flattened and dense layer is added followed by the output layer with single neuron. This neuron gives us value in the range of 0 to 1. We divide the classes by using threshold as 0.5.
* Once the model has been built and compiled, model is trained for 20 epochs.
* Model is optimized using Adam Optimizer and loss is calculated using Binary Cross Entropy.
* Finally, Achieved the accuracy of 97% on the test data.

<img width="446" alt="image" src="https://github.com/SharmilaAnanthasayanam/Hundred-and-Fifty-Rupees-Note-Classification/assets/112562560/ae10b243-5e8e-4cd8-af3d-edd9282a317a">


<img width="443" alt="image" src="https://github.com/SharmilaAnanthasayanam/Hundred-and-Fifty-Rupees-Note-Classification/assets/112562560/f4f45555-4b0d-41a3-b72a-e67008b0d3b5">





