# 🌿 PlantCure.ai
PlantCure.ai is a desktop application I built to learn how AI image classification works.
The idea started when I came across the New Plant Diseases Dataset on Kaggle. I wanted to see if I could train my own model and turn it into something that people could actually use instead of leaving it as just another notebook.
I trained a MobileNetV2 model using TensorFlow and then built a desktop application around it. The app works completely offline—you just select a leaf image and it predicts the disease, shows some information about it, and saves the result locally.
One challenge I faced was that I trained the model on my laptop without a dedicated GPU. Training took a long time, and sometimes it would stop before finishing. Because of that, I started using model checkpoints so I could continue training instead of starting over. That was one of the biggest things I learned while building this project.
---
What it can do
Detect 38 different plant diseases
Show the top 5 predictions with confidence scores
Display disease information and symptoms
Suggest organic and chemical treatments
Show prevention tips
Save prediction history locally
Export predictions as PDF reports
Work completely offline after installation

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

# How it works
Select a plant leaf image.
The image is resized to 128 × 128.
The trained MobileNetV2 model predicts the disease.
The application displays the top predictions with confidence scores.
Information about the predicted disease is loaded from a local database.
The prediction can be saved and exported as a PDF report.

# Dataset
I trained the model using the New Plant Diseases Dataset (Augmented) from Kaggle.
The dataset contains over 70,000 leaf images across 38 disease categories and healthy plant classes.

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


## About

This project was built as part of **Hack Club Stardance**.

Thanks for checking it out!
