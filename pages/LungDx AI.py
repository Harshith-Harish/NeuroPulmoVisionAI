import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import os

st.set_page_config(
    page_title="LungDx AI",
    page_icon="🫁",# You can use emojis as icons too
    layout="wide")


# global variable that will be used to store the interpreter
covid_interpreter = None
labels = {0: "COVID-19", 1: "Viral Pneumonia", 2: "Normal"}

def input_covid_classifier():
    # function to read the model from disk
    global covid_interpreter
    covid_interpreter = tf.lite.Interpreter(model_path=os.path.join(os.getcwd(), r'F:\Wipro Main\WILP\WASE\8th SEM\NeuroPulmoVisionAI\LungsDX_AI\covid_classifier.tflite'))
    covid_interpreter.allocate_tensors()

def predict(image):

    input_details = covid_interpreter.get_input_details()
    output_details = covid_interpreter.get_output_details()

    image = image.convert("RGB")
    image = image.resize((256, 256))
    img = np.array(image, dtype='float32')

    img = img/255
    img = img.reshape((1, 256, 256, 3))
    covid_interpreter.set_tensor(input_details[0]['index'], img)
    covid_interpreter.invoke()
    predictions = covid_interpreter.get_tensor(output_details[0]['index'])
    pred = np.argmax(predictions[0])
    result = {
        'class': labels[pred],
        'class_probablity': np.round(predictions[0][pred]*100,2)
    }

    return result

st.title("Chest X-ray Classification App")

if __name__ == '__main__':
    st.logo(r'F:\Wipro Main\WILP\WASE\8th SEM\NeuroPulmoVisionAI\lungs-symbol-icon-png.png', icon_image=r'F:\Wipro Main\WILP\WASE\8th SEM\NeuroPulmoVisionAI\lungDX.png')
    st.sidebar.header("Chest X-Ray Diagnose")
    st.sidebar.markdown("Chest X-Ray Diagnose uses a Convolutional Neural Network to detect COVID-19 and Viral Pneumonia in Chest X-Ray Images with an accuracy of 97%.")
    st.sidebar.subheader("Upload an image to get a diagnosis")
    st.sidebar.write('Made with ❤️ by Harshith')
    file= st.file_uploader("Select the image file", type=['jpg', 'jpeg', 'png'])
    
    #if file_uploaded is not None:
    if file:
        if st.button("Predict Output:"):
            with st.spinner("Predicting..."):
                if covid_interpreter is None:
                    input_covid_classifier()
                image = Image.open(file)
                result = predict(image)
                col1, col2 = st.columns(2)
                col2.image(image, caption="The image is classified as "+result['class'], width=300)
                col1.header("Classification Result")
                col1.write("The image is classified as "+result['class'])
                col1.write("The class probability is "+str(result['class_probablity'])+"%")
