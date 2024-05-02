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
* Once the model has been built and compiled, we fitted our data to the model.
* Achieved the accuracy of 97% on the test data.

<img width="473" alt="image" src="https://github.com/SharmilaAnanthasayanam/Hundred-and-Fifty-Rupees-Note-Classification/assets/112562560/95969934-b7d8-4c59-a50d-57b3c4f7cc4a">


<img width="443" alt="image" src="https://github.com/SharmilaAnanthasayanam/Hundred-and-Fifty-Rupees-Note-Classification/assets/112562560/f4f45555-4b0d-41a3-b72a-e67008b0d3b5">





