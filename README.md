# Neuropulmo Vision

## Overview

The **Neuropulmo Vision** is a machine learning application designed to assist in the diagnosis of medical conditions by analyzing medical images. This project focuses on two main functionalities: 
1. **Brain Tumor Segmentation** using the U-Net model.
2. **Chest X-ray Classification** using Convolutional Neural Networks (CNNs).

The system integrates both functionalities into a user-friendly interface developed with Streamlit, providing healthcare professionals with valuable diagnostic support.

## Features

- **Brain Tumor Segmentation**: Accurately identifies and segments brain tumor regions in MRI scans using a deep learning U-Net architecture.
- **Chest X-ray Classification**: Classifies chest X-ray images into categories (e.g., normal vs. abnormal) using a CNN model.
- **User-Friendly Interface**: A Streamlit-based web application allows users to upload images and view results easily.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Model Architecture](#model-architecture)
- [Results](#results)
- [Screenshots](#screenshots)

## Installation

To set up the project locally, follow these instructions:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/neuropulmo-vision.git

2. **Navigate to the project directory:**
   ```bash
   cd neuropulmo-vision

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   
4. **Usage**
   *To run the application, execute the following command:*
   ```bash
   streamlit run app.py
Once the application is running, open your browser and navigate to http://localhost:8501 to access the interface.

**Uploading Images**
Brain MRI: Upload an MRI scan to see the segmented tumor regions.
Chest X-ray: Upload a chest X-ray image to get classification results.
   
5.**Data**
The dataset used for training the models can be found here or can be downloaded from [source link].
Ensure that the dataset is placed in the data/ directory before running the application.

*Model Architecture*
U-Net for Brain Tumor Segmentation:
The U-Net model architecture is used for segmenting brain tumor regions. It is particularly effective for biomedical image segmentation tasks due to its encoder-decoder structure.
CNN for Chest X-ray Classification:
A Convolutional Neural Network (CNN) is employed for classifying chest X-ray images. The architecture consists of multiple convolutional layers followed by pooling and dense layers for accurate classification.
Results:

Brain Tumor Segmentation Accuracy: 98%
Chest X-ray Classification Accuracy: 97%

