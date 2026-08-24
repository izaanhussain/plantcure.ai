"""
Plant Disease Predictor Module
Handles model loading and disease prediction from images
"""

import os
import pickle
import numpy as np
from tensorflow import keras
from tensorflow.keras.utils import load_img, img_to_array
from PIL import Image
import cv2
import time

from utils import resource_path


def _raise_file_not_found(file_path, description):
    model_dir = os.path.dirname(file_path)
    if os.path.isdir(model_dir):
        try:
            contents = os.listdir(model_dir)
            folder_contents = "\n".join(sorted(contents)) or "(empty)"
        except Exception as list_error:
            folder_contents = f"(unable to list folder contents: {list_error})"
    else:
        folder_contents = "(folder does not exist)"

    raise FileNotFoundError(
        f"{description} not found.\n\n"
        f"Expected:\n{file_path}\n\n"
        f"Current Working Directory:\n{os.getcwd()}\n\n"
        f"Running in PyInstaller:\n{getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')}\n\n"
        f"Contents of model folder:\n{folder_contents}"
    )


class DiseasePredictor:
    """Handles plant disease prediction using trained model"""
    
    def __init__(self, model_path=None, class_indices_path=None):
        """
        Initialize the predictor with model and class indices
        
        Args:
            model_path: Path to the .h5 model file
            class_indices_path: Path to the class_indices.pkl file
        """
        self.model = None
        self.class_names = []
        self.input_size = (128, 128)

        self.model_path = resource_path(model_path or "model/plant_disease_transfer.h5")
        self.class_indices_path = resource_path(class_indices_path or "model/class_indices.pkl")

        self._load_model()
        self._load_class_indices()
    
    def _verify_path(self, path, description):
        if not os.path.exists(path):
            _raise_file_not_found(path, description)

    def _load_model(self):
        """Load the trained model"""
        try:
            self._verify_path(self.model_path, "Model file")
            self.model = keras.models.load_model(self.model_path)
        except Exception:
            raise
    
    def _load_class_indices(self):
        """Load class indices and create class names list"""
        try:
            self._verify_path(self.class_indices_path, "Class indices file")
            with open(self.class_indices_path, "rb") as f:
                class_indices = pickle.load(f)
            # Sort by index to get correct order
            self.class_names = [name for name, idx in sorted(class_indices.items(), key=lambda x: x[1])]
        except Exception:
            raise
    
    def preprocess_image(self, img_path):
        """
        Preprocess image for prediction
        
        Args:
            img_path: Path to image file or PIL Image object
            
        Returns:
            Preprocessed image array
        """
        try:
            if isinstance(img_path, str):
                # Load from file path
                img = load_img(img_path, target_size=self.input_size)
            elif isinstance(img_path, Image.Image):
                # Load from PIL Image
                img = img_path.resize(self.input_size)
            else:
                raise ValueError("Input must be file path or PIL Image")
            
            img_array = img_to_array(img)
            img_array = img_array / 255.0  # Normalize
            img_array = np.expand_dims(img_array, axis=0)
            return img_array
        except Exception:
            raise
    
    def predict(self, img_path, top_k=5):
        """
        Predict disease from image
        
        Args:
            img_path: Path to image file or PIL Image object
            top_k: Number of top predictions to return
            
        Returns:
            Dictionary with prediction results
        """
        start_time = time.time()
        
        try:
            # Preprocess image
            img_array = self.preprocess_image(img_path)
            
            # Make prediction
            predictions = self.model.predict(img_array, verbose=0)
            
            # Get top k predictions
            top_indices = np.argsort(predictions[0])[-top_k:][::-1]
            top_predictions = []
            
            for idx in top_indices:
                class_name = self.class_names[idx]
                confidence = float(predictions[0][idx]) * 100
                top_predictions.append({
                    'class': class_name,
                    'confidence': confidence
                })
            
            prediction_time = time.time() - start_time
            
            return {
                'success': True,
                'top_prediction': top_predictions[0],
                'all_predictions': top_predictions,
                'prediction_time': round(prediction_time, 3)
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'top_prediction': None,
                'all_predictions': [],
                'prediction_time': 0
            }
    
    def get_class_count(self):
        """Return total number of disease classes"""
        return len(self.class_names)
    
    def get_class_names(self):
        """Return list of all class names"""
        return self.class_names


# Singleton instance for app-wide use
_predictor_instance = None


def get_predictor():
    """Get or create singleton predictor instance"""
    global _predictor_instance
    if _predictor_instance is None:
        _predictor_instance = DiseasePredictor()
    return _predictor_instance
