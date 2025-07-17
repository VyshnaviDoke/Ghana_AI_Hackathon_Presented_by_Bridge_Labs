# Ghana_AI_Hackathon_Presented_by_Bridge_Labs
Smart Agriculture: Crop Disease Detection
This project provides an AI-powered solution to detect and classify crop diseases affecting key Ghanaian crops (cashew, cassava, maize, tomato) using images from smartphones or drones.

Features
- Upload an image of a leaf to detect disease
- Deep learning model predicts crop type and disease class
- Simple and clean Flask-based web interface

Here is the dataset download link https://www.kaggle.com/datasets/rahimanshu/ccmt-plant-disease-dataset

Project Structure
├── app.py # Flask backend
├── model.h5 # Trained Keras model
├── static/
│ └── style.css # Stylesheet
  └── uploads
  └── bkgimg # backgroundimage
├── templates/
│ └── index.html # Frontend page
├── requirements.txt # Python dependencies

How to Run Locally

1. Clone the Repository
2. Create a Virtual Environment
   python -m venv venv
   venv\Scripts\activate
3.Install Dependencies
Make sure you have pip installed
   pip install -r requirements.txt
4.Run the Project
   python app.py

