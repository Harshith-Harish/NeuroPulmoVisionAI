import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from tensorflow.keras import backend as K
from tensorflow.keras.models import load_model
import cv2

st.set_page_config(
    page_title="BrainDx AI",
    page_icon="🧠",# You can use emojis as icons too
    layout="wide")  


plt.style.use("ggplot")

def dice_coefficients(y_true, y_pred, smooth=100):
    y_true_flatten = K.flatten(y_true)
    y_pred_flatten = K.flatten(y_pred)

    intersection = K.sum(y_true_flatten * y_pred_flatten)
    union = K.sum(y_true_flatten) + K.sum(y_pred_flatten)
    return (2 * intersection + smooth) / (union + smooth)

def dice_coefficients_loss(y_true, y_pred, smooth=100):
    return -dice_coefficients(y_true, y_pred, smooth)

def iou(y_true, y_pred, smooth=100):
    intersection = K.sum(y_true * y_pred)
    sum = K.sum(y_true + y_pred)
    iou = (intersection + smooth) / (sum - intersection + smooth)
    return iou

def jaccard_distance(y_true, y_pred):
    y_true_flatten = K.flatten(y_true)
    y_pred_flatten = K.flatten(y_pred)
    return -iou(y_true_flatten, y_pred_flatten)

st.title("Brain MRI Segmentation App")
model = load_model(r"F:\Wipro Main\WILP\WASE\8th SEM\NeuroPulmoVisionAI\BrainDX_AI\unet_brain_mri_seg.hdf5", custom_objects={
        'dice_coef_loss': dice_coefficients_loss, 'iou': iou, 'dice_coef': dice_coefficients})

def load_image(file):
    content = file.getvalue()
    image = np.asarray(bytearray(content), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

def preprocess_image(image):
    im_height = 256
    im_width = 256
    img2 = cv2.resize(image, (im_height, im_width))
    Img3 = img2 / 255
    img4 = Img3[np.newaxis, :, :, :]
    return img4

def predict_image(img4):
    pred_img = model.predict(img4)
    return pred_img

if __name__ == '__main__':
    st.logo(r'F:\Wipro Main\WILP\WASE\8th SEM\NeuroPulmoVisionAI\Brain_icon.png', icon_image=r'F:\Wipro Main\WILP\WASE\8th SEM\NeuroPulmoVisionAI\brainDX.png')
    st.sidebar.header("Brain Tumor MRI Segmentation")
    st.sidebar.markdown("Brain Tumor MRI Segmentation uses a U-Net Architecture to detect Brain Tumor region in Brain MRI Images with an accuracy of 97%.")
    st.sidebar.subheader("Upload an image to get Brain Tumor region")
    #st.sidebar.write('Made with ❤️ by Harshith')

    file = st.file_uploader("Select the image file", type=["jpg", "png", "jpg"])

    if file:
        col1, col2 = st.columns(2)
        col1.header("Original Image:")
        col1.image(file, caption="Brain MRI Image",width=300)
        image = load_image(file)
        img4 = preprocess_image(image)
        
        if st.button("Predict Output:"):
            with st.spinner("Predicting..."):
            #st.write("Waiting for prediction...")
                try:
                    pred_img = predict_image(img4)
                    col2.header("Predicted Image:")
                    col2.image(pred_img,caption="The image shows the region of tumor if exists in the uploaded MRI Image", width=300)
                except Exception as e:
                    st.error(f"Error: {e}")            