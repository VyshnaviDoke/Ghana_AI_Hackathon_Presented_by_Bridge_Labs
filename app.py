import os
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Load the trained model
model = load_model('plant_disease_model.h5')
IMG_SIZE = (224, 224)  # Adjust to your model's input size

# Define class names
CLASS_NAMES = {
    0: 'All_healthy_Cashew_healthy',
    1: 'All_healthy_Cassava_healthy',
    2: 'All_healthy_Maize_healthy',
    3: 'All_healthy_Tomato_healthy',
    4: 'diseased_Cashew_anthracnose',
    5: 'diseased_Cashew_gumosis',
    6: 'diseased_Cashew_leaf miner',
    7: 'diseased_Cashew_red rust',
    8: 'diseased_Cassava_bacterial blight',
    9: 'diseased_Cassava_brown spot',
    10: 'diseased_Cassava_green mite',
    11: 'diseased_Cassava_mosaic',
    12: 'diseased_Maize_fall armyworm',
    13: 'diseased_Maize_grasshoper',
    14: 'diseased_Maize_leaf beetle',
    15: 'diseased_Maize_leaf blight',
    16: 'diseased_Maize_leaf spot',
    17: 'diseased_Maize_streak virus',
    18: 'diseased_Tomato_leaf blight',
    19: 'diseased_Tomato_leaf curl',
    20: 'diseased_Tomato_septoria leaf spot',
    21: 'diseased_Tomato_verticulium wilt'
}

def process_image(img_path):
    img = image.load_img(img_path, target_size=IMG_SIZE)
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    image_url = None

    if request.method == 'POST':
        img_file = request.files['image']
        if img_file:
            path = os.path.join(app.config['UPLOAD_FOLDER'], img_file.filename)
            img_file.save(path)

            img_data = process_image(path)
            pred = model.predict(img_data)
            label_index = int(np.argmax(pred))
            confidence = float(np.max(pred)) * 100
            label_name = CLASS_NAMES.get(label_index, "Unknown")

            prediction = f"Predicted class: {label_name} (Confidence: {confidence:.2f}%)"
            image_url = path

    return render_template('index.html', prediction=prediction, image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)
