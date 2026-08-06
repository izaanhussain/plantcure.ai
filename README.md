# 🌿 PlantCure.ai

<div align="center">

**AI-Powered Plant Disease Detection**

*A modern, professional AI application for identifying plant diseases using deep learning*

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)](https://www.tensorflow.org/)
[![Gradio](https://img.shields.io/badge/Gradio-Latest-red)](https://gradio.app/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Screenshots](#-screenshots) • [Project Structure](#-project-structure) • [Technical Details](#-technical-details)

</div>

---

## 🚀 Overview

**PlantCure.ai** is a production-ready AI application that detects plant diseases from leaf images using advanced deep learning. Built with a modern, responsive interface and professional architecture, it's designed for farmers, researchers, and plant enthusiasts who need quick, accurate disease identification.

The application uses a **MobileNetV2** transfer learning model trained on the **New Plant Diseases Dataset (Augmented)** containing 70,000+ images across 38 disease classes covering various crops including tomatoes, potatoes, corn, grapes, apples, and more.

### ✨ Key Highlights

- 🎯 **38 Disease Classes** - Comprehensive coverage of common plant diseases
- ⚡ **Real-time Prediction** - Fast inference using optimized TensorFlow model
- 🎨 **Modern UI** - Beautiful glassmorphism design with dark theme
- 📱 **Responsive** - Works on desktop, tablet, and mobile devices
- 💾 **Local History** - SQLite database stores all predictions offline
- 📄 **PDF Reports** - Generate professional reports with treatment recommendations
- 🌙 **Dark/Light Mode** - Customizable theme for comfortable viewing
- 🔒 **Privacy-Focused** - Runs completely offline, no data leaves your device

---

## 🌟 Features

### 🔍 Disease Detection
- **Multi-class Classification** - Identifies 38 different plant diseases
- **Top 5 Predictions** - Shows confidence scores for all likely diseases
- **Real-time Analysis** - Get results in under 1 second
- **Confidence Metrics** - Clear probability percentages for each prediction

### 📤 Flexible Input Methods
- **Drag & Drop** - Intuitive file upload interface
- **File Browser** - Traditional file selection
- **Image Preview** - See your image before analysis

### 📋 Comprehensive Disease Information
- **Scientific Names** - Accurate botanical nomenclature
- **Detailed Descriptions** - Understand what each disease is
- **Symptoms Guide** - Know what to look for
- **Causes** - Understand disease origins
- **Treatment Options**:
  - Organic treatments for eco-friendly solutions
  - Chemical treatments for severe cases
- **Prevention Tips** - Protect your plants proactively
- **Difficulty Levels** - Assess treatment complexity

### 📜 Prediction History
- **Automatic Saving** - Every prediction is stored locally
- **Timestamp Tracking** - Know when each prediction was made
- **Thumbnail Previews** - Visual history of analyzed images
- **Search & Filter** - Find specific predictions easily
- **Bulk Management** - Clear history when needed

### 📄 PDF Report Generation
- **Professional Reports** - Export results as formatted PDFs
- **Complete Information** - Includes disease details and treatments
- **Branding** - PlantCure.ai branded reports
- **Timestamp** - Automatically dated reports
- **Downloadable** - Save and share reports

### ⚙️ Settings & Maintenance
- **Theme Toggle** - Switch between dark and light modes
- **File Management** - Clean up old files automatically
- **Statistics Dashboard** - View prediction analytics
- **Top Diseases** - See most frequently detected conditions
- **Performance Metrics** - Track average confidence scores

### 🎨 Modern User Interface
- **Glassmorphism Design** - Modern frosted glass aesthetic
- **Gradient Accents** - Beautiful color schemes
- **Smooth Animations** - Fluid transitions and interactions
- **Responsive Layout** - Adapts to any screen size
- **Professional Typography** - Clean, readable fonts
- **Intuitive Navigation** - Easy-to-use interface

---

## 📦 Installation

### Prerequisites

- **Python 3.10 or higher**
- **pip** package manager
- **4GB+ RAM** recommended
- **2GB+ disk space**

### Step 1: Clone or Download

```bash
# If cloning from git
git clone https://github.com/yourusername/plantcure.ai.git
cd plantcure.ai

# Or download and extract the ZIP file
# Navigate to the extracted directory
cd plantcure.ai
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Verify Installation

```bash
# Check if model files exist
ls model/

# You should see:
# - plant_disease_transfer.h5
# - plant_disease_checkpoint.h5
# - class_indices.pkl
```

### Step 4: Run the Application

```bash
python app.py
```

The application will automatically open in your default browser at `http://127.0.0.1:7860`

---

## 🎮 Usage

### Quick Start

1. **Launch the Application**
   ```bash
   python app.py
   ```

2. **Upload an Image**
   - Drag and drop a plant leaf image onto the upload area
   - Or click "Browse" to select a file

3. **Get Prediction**
   - Click the "🔍 Predict Disease" button
   - View the prediction results with confidence scores
   - Read detailed disease information

4. **Generate Report** (Optional)
   - Click "📄 Generate PDF Report"
   - Download the professional PDF report

### Using the Interface

#### Main Features

- **Upload Section**: Left panel for image input
- **Results Section**: Right panel showing predictions and disease details
- **History Panel**: Bottom left for prediction history
- **Statistics Panel**: Bottom center for analytics
- **Settings Panel**: Bottom right for app settings

#### Tips for Best Results

- **Good Lighting**: Use well-lit, clear images
- **Focus on Affected Areas**: Capture the diseased parts clearly
- **Multiple Angles**: If possible, photograph from different angles
- **High Resolution**: Use higher resolution images for better accuracy
- **Clean Background**: Simple backgrounds help with analysis

---

## 📸 Screenshots

### Main Interface
*Modern glassmorphism design with intuitive layout*

### Prediction Results
*Clear confidence scores and detailed disease information*

### Disease Details
*Comprehensive information including treatments and prevention*

### History Dashboard
*Track all your predictions with timestamps and thumbnails*

### PDF Report
*Professional, branded reports for documentation*

---

## 🏗️ Project Structure

```
PlantCure.ai/
│
├── app.py                      # Main application entry point
├── predictor.py                # Disease prediction logic
├── database.py                 # SQLite database management
├── disease_database.py         # Disease information database
├── utils.py                    # Utility functions (PDF, images, etc.)
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── LICENSE                     # MIT License
│
├── model/                      # Model files
│   ├── plant_disease_transfer.h5
│   ├── plant_disease_checkpoint.h5
│   └── class_indices.pkl
│
├── assets/                     # Static assets (icons, etc.)
├── history/                    # Prediction history database
│   └── predictions.db
├── reports/                    # Generated PDF reports
│
└── (Original training files - preserved)
    ├── train_transfer.py
    ├── predict_transfer.py
    ├── create_classes.py
    └── Requirements.txt
```

---

## 🔬 Technical Details

### Model Architecture

- **Base Model**: MobileNetV2 (ImageNet pre-trained)
- **Transfer Learning**: Custom classification head
- **Input Size**: 128×128 RGB images
- **Output**: 38 disease classes
- **Training Dataset**: 70,000+ augmented images
- **Framework**: TensorFlow/Keras

### Disease Classes

The model can detect diseases in the following crops:

- **Apple**: Scab, Black Rot, Cedar Apple Rust, Healthy
- **Blueberry**: Healthy
- **Cherry**: Powdery Mildew, Healthy
- **Corn**: Cercospora Leaf Spot, Common Rust, Northern Leaf Blight, Healthy
- **Grape**: Black Rot, Esca (Black Measles), Leaf Blight, Healthy
- **Orange**: Huanglongbing (Citrus Greening)
- **Peach**: Bacterial Spot, Healthy
- **Pepper**: Bacterial Spot, Healthy
- **Potato**: Early Blight, Late Blight, Healthy
- **Raspberry**: Healthy
- **Soybean**: Healthy
- **Squash**: Powdery Mildew
- **Strawberry**: Leaf Scorch, Healthy
- **Tomato**: Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Septoria Leaf Spot, Spider Mites, Target Spot, Yellow Leaf Curl Virus, Mosaic Virus, Healthy

### Technology Stack

- **Backend**: Python 3.10+
- **Deep Learning**: TensorFlow 2.x
- **Image Processing**: OpenCV, Pillow
- **UI Framework**: Gradio
- **Database**: SQLite
- **PDF Generation**: ReportLab
- **Visualization**: Matplotlib
- **Numerical Computing**: NumPy

### Performance

- **Prediction Time**: < 1 second on modern CPU
- **Model Size**: ~35MB
- **Memory Usage**: ~500MB RAM
- **Accuracy**: 95%+ on test dataset

---

## 🛠️ Development

### Adding New Diseases

1. **Retrain the Model**
   - Prepare your dataset
   - Use `train_transfer.py` as a template
   - Update `class_indices.pkl`

2. **Update Disease Database**
   - Add entries to `disease_database.py`
   - Include comprehensive information for each disease

3. **Test Thoroughly**
   - Validate predictions
   - Check disease information accuracy
   - Test UI integration

### Customizing the UI

Edit the CSS in `app.py` to customize:
- Color schemes
- Layout structure
- Typography
- Animations

### Extending Features

The modular architecture makes it easy to add:
- Additional input methods
- New export formats
- Enhanced analytics
- Multi-language support

---

## 📝 API Reference

### Predictor Class

```python
from predictor import get_predictor

predictor = get_predictor()
result = predictor.predict(image_path, top_k=5)
```

### Database Class

```python
from database import get_database

db = get_database()
predictions = db.get_all_predictions()
```

### Disease Database

```python
from disease_database import get_disease_db

db = get_disease_db()
info = db.get_disease_info('Tomato___Early_blight')
```

---

## 🤝 Contributing

Contributions are welcome! Areas for improvement:

- Additional disease classes
- UI enhancements
- Performance optimizations
- Bug fixes
- Documentation improvements

Please read the existing code and follow the established patterns before submitting pull requests.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Dataset**: [New Plant Diseases Dataset (Augmented)](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset) on Kaggle
- **TensorFlow**: Deep learning framework
- **Gradio**: UI framework
- **MobileNetV2**: Pre-trained model architecture

---

## 📧 Support

For issues, questions, or suggestions:

- Open an issue on GitHub
- Check existing documentation
- Review the code comments

---

## 🌱 Future Roadmap

- [ ] Mobile application (iOS/Android)
- [ ] Additional disease classes
- [ ] Multi-language support
- [ ] Cloud synchronization (optional)
- [ ] Community disease database
- [ ] API for third-party integration
- [ ] Batch image processing

---

<div align="center">

**Built with ❤️ for the Hack Club Stardance**

*Empowering farmers with AI technology*

[🔝 Back to Top](#-plantcureai)

</div>
