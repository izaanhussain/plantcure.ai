# 🌿 Plant Disease Detection AI

## 🚀 Overview
**Plant Disease Detection AI** is a deep learning model trained to identify multiple plant diseases from leaf images.  
Built using **TensorFlow** and **MobileNetV2**, it classifies plant diseases with high accuracy, helping farmers and researchers quickly identify issues and take action.

This project is trained on the **New Plant Diseases Dataset (Augmented)** from **Kaggle**, containing **70,000+ high-quality images** of healthy and diseased plant leaves across multiple species.

---

## 🧠 Features
- 🌱 Detects **dozens of plant diseases** automatically from leaf photos.  
- ⚡ Uses **transfer learning (MobileNetV2)** for high accuracy and fast prediction.  
- 💾 Includes model checkpointing to save progress during training.  
- 🧩 Simple prediction script — drag & drop your image to get instant results.  
- 🧰 Open-source and ready for integration into mobile or IoT systems (e.g., smart farms, agricultural robots).

---

## 🏗️ Tech Stack
- **TensorFlow / Keras**
- **NumPy**
- **Pillow**
- **MobileNetV2 (ImageNet pretrained)**
- **Python 3.8+**

---

## 📂 Dataset
📊 **Dataset:** [New Plant Diseases Dataset (Augmented) – Kaggle](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset)  
📸 **Total Images:** ~70,000  
🌾 **Classes:** Healthy and diseased leaves from multiple plants (tomato, corn, potato, grape, etc.)

---
## 🧪 Training & Prediction

### 🧠 Train the Model
Run the following command to start training:

```bash
python train_transfer.py

---
## 🧪 Predicting Code 
Run the following command to start predicting the disease

```bash
python predict_transfer.py
