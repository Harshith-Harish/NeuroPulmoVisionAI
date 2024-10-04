import streamlit as st



def show_introduction():
    st.set_page_config(
        page_title="NeuroPulmoVisionAI",
        page_icon="ct-scan.icns",  # You can use emojis as icons too
        layout="wide",  # Can be "centered" or "wide"
        initial_sidebar_state="auto")  # Can be "auto", "expanded", "collapsed"layout="wide"))
    
    st.logo('NeuroPulmoVisionAI.png',icon_image='NeuroPulmoVisionAI.png')
    st.sidebar.header("Select the Diagnosis tool required.....")
    st.title("NeuroPulmoVisionAI")
    st.header("Brain MRI and Lung X-ray classification with Deep Learning")
    st.write("""
	Welcome to the Brain MRI Segmentation and Lung X-Ray Classification Application.
    This app utilizes deep learning technology to support the diagnosis of neurological and respiratory conditions through 
    medical imaging data. By employing sophisticated neural network models, our goal is to offer precise and effective 
    diagnostic tools for healthcare professionals.
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.header("Brain Diagnosis to predict the Tumor Region")
        st.write("""
		Magnetic Resonance Imaging (MRI) is a non-invasive method for generating detailed 
		images of the brain and other body parts. In this application, we utilize deep learning models to 
		examine brain MRI scans for identifying abnormalities such as tumors, lesions, and various neurological conditions.
        """)
        st.image(r"lBrain_MRI.png", caption="Sample of Brain MRI Image", width=500)

    with col2:
        st.header("Lungs Diagnosis for Phenomonic/Covid-19 Infection")
        st.write("""
        Chest X-rays are frequently employed to diagnose and track conditions related to the chest, 
		its contents, and surrounding structures. Our deep learning models are designed to detect a 
		range of lung conditions, including pneumonia, tuberculosis, and lung cancer, from X-ray images.
        """)
        st.image(r"Lung_Xray.png", caption="Sample of Lungs X-ray Image", width=600)

    st.header("Deep Learning in Medical Imaging")
    st.write("""
	Deep learning, a branch of artificial intelligence (AI), focuses on training neural networks 
	with extensive data to identify patterns and make predictions. In medical imaging, deep learning 
	models can support radiologists by offering a second opinion, highlighting key areas, 
	and enhancing both diagnostic precision and efficiency.
    """)

    st.write("""
	This application is developed with Streamlit, a robust framework for building 
	interactive web applications in Python. We aim for this app to offer valuable 
	insights and assist in the diagnosis and treatment of patients.
    """)

if __name__ == "__main__":
    show_introduction()
