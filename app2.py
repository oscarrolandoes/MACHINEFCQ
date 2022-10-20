import streamlit as st
from img_classification import teachable_machine_classification
import keras
from PIL import Image, ImageOps
import numpy as np

st.title("BRAIN TUMORS IMAGE RECOGNIZER")

uploaded_file = st.file_uploader("Carga una imagen ...", type=["jpg","jpeg"])
if uploaded_file is not None:
  image = Image.open(uploaded_file)
  st.image(image)
  label = teachable_machine_classification(image, 'keras_model.h5')
  if label == 0:
    st.write("YES TUMORAL FORMATIONS")

  else:
    st.write("NO, TUMORAL FORMATIONS")
