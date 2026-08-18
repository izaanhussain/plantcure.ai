# 🌿 PlantCure.ai

> AI-powered plant disease detection using TensorFlow and MobileNetV2.

I built PlantCure.ai to learn how image classification works using tensorflow I trained a MobileNetV2 model on the New Plant Diseases Dataset from Kaggle and then created a desktop application that can identify plant diseases from leaf images without an internet connection. This project taught me how to train models, save checkpoints as i had no dedicated gpu the training would be stopped in between so checkpoints helmed me to save the progress, and connect an AI model to a real application.

---

## Features

- 🌱 Detects **38 plant diseases**
- 🎯 **92% validation accuracy**
- 🧠 MobileNetV2 Transfer Learning model
- 📈 Displays Top-5 predictions with confidence scores
- 📖 Disease description and symptoms
- 💊 Organic & chemical treatment suggestions
- 🛡 Prevention tips
- 📄 Export prediction as PDF
- 🗂 Stores prediction history locally
- 💻 Runs completely offline

---

## Screenshots

<img width="1891" height="892" alt="image" src="https://github.com/user-attachments/assets/5bfb07d4-6fe8-4df7-b2b2-d17e88aa665e" />


### Home

<img width="1891" height="892" alt="image" src="https://github.com/user-attachments/assets/33fec4b2-d408-48ff-970c-6e2dd6556830" />


### Prediction

<img width="1856" height="902" alt="image" src="https://github.com/user-attachments/assets/e20a7852-b133-4660-b86e-7caf6ed8812b" />


### History

<img width="1882" height="772" alt="image" src="https://github.com/user-attachments/assets/a4b69926-8fcb-4ff7-9d05-2fcdc5a022d9" />


### PDF Report

<img width="608" height="767" alt="image" src="https://github.com/user-attachments/assets/a0e66a91-d96b-4547-886c-ad5cf23057ba" />


---

# Model

| Property | Value |
|----------|-------|
| Architecture | MobileNetV2 |
| Learning Method | Transfer Learning |
| Framework | TensorFlow / Keras |
| Dataset | New Plant Diseases Dataset (Augmented) |
| Classes | 38 |
| Validation Accuracy | **92%** |
| Input Size | 128 × 128 |
| Prediction Time | <1 second (CPU) |

---

# Dataset

This project was trained using the **New Plant Diseases Dataset (Augmented)** available on Kaggle.

Dataset contains over **70,000** images covering **38 different plant disease classes** including:

- Apple
- Tomato
- Potato
- Corn
- Grape
- Strawberry
- Orange
- Peach
- Pepper
- Cherry
- Blueberry
- Soybean
- Raspberry
- Squash

---

# Tech Stack

- Python
- TensorFlow
- Keras
- OpenCV
- Pillow
- NumPy
- SQLite
- ReportLab
- Gradio
- PyInstaller

---

# Project Structure

```text
PlantCure.ai
│
├── app.py
├── predictor.py
├── database.py
├── disease_database.py
├── utils.py
├── check_model.py
├── requirements.txt
├── README.md
├── PlantCure.spec
│
├── model/
│   ├── plant_disease_transfer.h5
│   ├── plant_disease_checkpoint.h5
│   └── class_indices.pkl
│
├── assets/
├── history/
├── reports/
│
└── archive/
    ├── train_transfer.py
    ├── predict_transfer.py
    └── create_classes.py
```

---

# Installation

Clone the repository.

```bash
git clone https://github.com/izaanhussain/plantcure.ai.git
```

Open the project.

```bash
cd plantcure.ai
```

Install dependencies.

```bash
pip install -r Requirements.txt
```

Run the application.

```bash
python app.py
```

---

# How it Works

1. Upload a plant leaf image.
2. The image is resized to **128×128**.
3. The TensorFlow model performs inference.
4. The Top-5 predictions are generated.
5. Disease information is retrieved from the local database.
6. The prediction is saved locally.
7. A PDF report can be exported.

---

## About

This project was built as part of **Hack Club Stardance**.

The goal was not only to train an AI model but to build a complete desktop application that anyone can use to identify plant diseases without requiring an internet connection.

If you found this project interesting, consider giving it a ⭐.
