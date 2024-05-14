import streamlit as st
import cv2 as cv
import numpy as np
import tensorflow as tf
from tensorflow.keras.metrics import F1Score

st.title("Hundred and Fifty Rupees Classification")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file:
  bytes_data = uploaded_file.getvalue()
  #Convert Bytes data to image array
  image_array = np.frombuffer(bytes_data, dtype=np.uint8)
  image = cv.imdecode(image_array, flags=cv.IMREAD_COLOR)
  image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
  st.image(image)
  #image resizing
  resized_img = cv.resize(image, (256, 256))
  #image rescaling
  rescaled_img = resized_img/255

  #Model Loading and Prediction
  input_data = np.expand_dims(rescaled_img, axis=0)
  model = tf.keras.models.load_model('/content/drive/MyDrive/Models/NoteClassificationModel_Aug.h5')
  predictions = model.predict(input_data)
  if predictions >= 0.5:
    st.subheader("**:green[It is a Hundred Rupees Note]**")
  elif predictions < 0.5:
    st.subheader("**:green[It is a Fifty Rupees Note]**")