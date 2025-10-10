from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import pickle
import os

# Load model
model = load_model("plant_disease_transfer.h5")

# Load class indices
with open("class_indices.pkl", "rb") as f:
    class_indices = pickle.load(f)
class_names = list(class_indices.keys())

def predict_disease(img_path):
    img = image.load_img(img_path, target_size=(128, 128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    pred = model.predict(img_array)
    class_index = np.argmax(pred)
    confidence = pred[0][class_index] * 100
    return class_names[class_index], confidence

print("👉 Drag and drop an image file here, then press Enter:")
raw_input = input().strip()

# 🧹 Clean up PowerShell's weird formatting (& 'path')
if raw_input.startswith("&"):
    raw_input = raw_input.replace("&", "").strip()
if raw_input.startswith("'") or raw_input.startswith('"'):
    raw_input = raw_input.strip("'").strip('"')
if raw_input.startswith(" "):
    raw_input = raw_input.strip()

image_path = raw_input

# Check file
if not os.path.exists(image_path):
    print(f"❌ File not found: {image_path}")
else:
    disease, conf = predict_disease(image_path)
    print(f"\n✅ Predicted Disease: {disease}")
    print(f"🔍 Confidence: {conf:.2f}%")
