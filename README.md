## Overview

The **NeuropulmoVisionAI** is a machine learning application designed to assist in the diagnosis of medical conditions by analyzing medical images. This project is part of my Dissertation for MTech in Software Systems from BITS Pilani.  

This project focuses on two main functionalities:  
1. **Brain Tumor Segmentation** using the U-Net model.
2. **Chest X-ray Classification** using Convolutional Neural Networks (CNNs).

The system integrates both functionalities into a user-friendly interface developed with Streamlit, providing healthcare professionals with valuable diagnostic support.

## Project Status

**This project is currently in development:** 

While the core functionalities (Brain Tumor Segmentation and Chest X-ray Classification) are implemented, additional features, improvements, and optimizations are planned for future releases. 
Contributions, feedback, and suggestions are welcome as we continue to enhance the system.

## Features

- **Brain Tumor Segmentation**: Accurately identifies and segments brain tumor regions in MRI scans using a deep learning U-Net architecture.
- **Chest X-ray Classification**: Classifies chest X-ray images into categories (e.g., normal vs. abnormal) using a CNN model.
- **User-Friendly Interface**: A Streamlit-based web application allows users to upload images and view results easily.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Model Architecture](#model-architecture)
- [Results](#results)
- [Screenshots](#screenshots)
- [Tech Stack](#Tech-Stack)

## Installation

To set up the project locally, follow these instructions:

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/neuropulmo-vision.git
   ```
2. **Navigate to the project directory:**
   ```
   cd neuropulmo-vision
   ```
3. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```
## Usage
   *To run the application, execute the following command:*
   ```
   streamlit run Introduction.py
   ```
   Once the application is running, open your browser and navigate to http://localhost:8501 to access the interface.

   **Uploading Images**
   Brain MRI: Upload an MRI scan to see the segmented tumor regions.
   Chest X-ray: Upload a chest X-ray image to get classification results.

## Data

Brain MRI Dataset - [click here](https://www.kaggle.com/datasets/mateuszbuda/lgg-mri-segmentation/data)  

Chest X-ray Dataset - [click here](https://www.kaggle.com/datasets/amanullahasraf/covid19-pneumonia-normal-chest-xray-pa-dataset)  
   
## Model Architecture
**U-Net for Brain Tumor Segmentation:**
The U-Net model architecture is used for segmenting brain tumor regions. It is particularly effective for biomedical image segmentation tasks due to its encoder-decoder structure.

![5  U-Net_Architecture](https://github.com/user-attachments/assets/1896cb7c-7478-43d4-8be6-d9bbe89e7c1a)  
*U-Net Architecture*

**CNN for Chest X-ray Classification:**
A Convolutional Neural Network (CNN) is employed for classifying chest X-ray images. The architecture consists of multiple convolutional layers followed by pooling and dense layers for accurate classification.

![6  CNN_Architecture](https://github.com/user-attachments/assets/5f8553e2-d475-4c7c-9e9e-ff3a097c0cf5)  
*CNN Architecture*

## Results:

Brain Tumor Segmentation Accuracy: 98%  
Chest X-ray Classification Accuracy: 97%
   
## Screenshots:

![1  NeuroPulmoVisionAI_Introduction_Page](https://github.com/user-attachments/assets/27ed0bf1-e26a-4e5c-8676-4250d762afde)  
*NeuroPulmoVisionAI_Introduction_Page*

![2  NeuroPulmoVisionAI_Introduction_Page_without_Sidebar](https://github.com/user-attachments/assets/abc7da4d-7231-4d6d-b88a-303630064b84)  
*NeuroPulmoVisionAI_Introduction_Page_without_Sidebar*

![3  Brain_MRI_Segmentation_(BrainDX)_Page](https://github.com/user-attachments/assets/5990b480-dc9c-4d41-b7d1-4e90358d8f9a)  
*Brain_MRI_Segmentation_(BrainDX)_Page*

![4  Chest_X-Ray_Classification_(LungDX)_Page](https://github.com/user-attachments/assets/3bcfc12c-89ce-4fb5-b62d-8750e97b051c)
*Chest_X-Ray_Classification_(LungDX)_Page*

## Tech Stack:
<img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white"/> <img alt="Tensorflow" src="https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white"/> <img alt="Keras" src="https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white"/> <img alt="OpenCV" src="https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white"/>

