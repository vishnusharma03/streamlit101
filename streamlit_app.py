import streamlit as st
from endpoint import Query as Q
import numpy as np
from PIL import Image
import os
import pickle

# Page title and headers
st.title("Image Classification App")
st.header("Choose an image to classify:")

# Upload image
uploaded_file = st.file_uploader(" ", type=['png', 'jpeg', 'jpg'])

# Nice placeholder if no image
if uploaded_file is None:
    st.write("Upload an image to get started!")

# If image is uploaded
else:
    #with open(uploaded_file, 'rb') as f:
    bytes_data = uploaded_file.read()
    input_img = Image.open(uploaded_file)
    #img_bytes = input_img.tobytes()
    # Get model prediction (Dummy code here)
    Query = Q('jumpstart-dft-endpoint102')
    response = Query.query_endpoint(bytes_data)
    pred_label = Query.parse_prediction(response)

    # Display image and results
    col1, col2 = st.columns(2)
    with col1:
        st.image(input_img, width=250)
    with col2:
        st.success(f"Predicted label: {pred_label}")


# Predict function
@st.cache
def predict(img):
    # Dummy predict function
    return np.random.choice(['Cat', 'Dog', 'Horse'])

