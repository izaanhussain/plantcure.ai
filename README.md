# 🌿 PlantCure.ai

> AI-powered plant disease detection using TensorFlow and MobileNetV2.

PlantCure.ai is a desktop application that identifies plant diseases from leaf images using a deep learning model trained with Transfer Learning. The project is built entirely in Python and runs completely offline after installation.

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

# Future Improvements

- Android application
- iOS application
- Batch image prediction
- More plant species
- REST API
- Cloud synchronization (optional)
- Multi-language support

---

# License

This project is licensed under the MIT License.

---

# Acknowledgements

- TensorFlow
- Gradio
- MobileNetV2
- ReportLab
- New Plant Diseases Dataset (Augmented)

---

## About

This project was built as part of **Hack Club Stardance**.

The goal was not only to train an AI model but to build a complete desktop application that anyone can use to identify plant diseases without requiring an internet connection.

If you found this project interesting, consider giving it a ⭐.
