import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import os


class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        
        model_path = os.path.join("artifacts", "training", "model.h5")
        model = load_model(model_path)

    
        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)

  
        test_image = preprocess_input(test_image)

  
        probability = model.predict(test_image)[0][0]

    
        if probability > 0.5:
            prediction = 'Fake'
            confidence = float(probability * 100)
        else:
            prediction = 'Real'
            confidence = float((1 - probability) * 100)

        print(f"Prediction: {prediction}, Confidence: {confidence:.2f}%")

        return [{ 
            "image": prediction, 
            "confidence": f"{confidence:.2f}%" 
        }]