"""
PlantCure.ai - Main Application
Modern AI-powered plant disease detection application
"""

import copy
import gradio as gr
import os
import socket
import sys
import logging
import tempfile
from datetime import datetime
from PIL import Image
import numpy as np

# Import custom modules
from predictor import get_predictor
from disease_database import get_disease_db
from database import get_database
from utils import (
    save_thumbnail, generate_pdf_report, format_disease_name,
    get_confidence_color, validate_image_file, format_timestamp,
    create_directories
)


class PlantCureApp:
    """Main application class for PlantCure.ai"""
    
    def __init__(self):
        """Initialize the application"""
        # Create necessary directories
        create_directories()
        
        # Initialize modules
        self.predictor = get_predictor()
        self.disease_db = get_disease_db()
        self.database = get_database()
        
        print("[OK] PlantCure.ai initialized successfully")
    
    def predict_image(self, image_input):
        """
        Predict disease from uploaded image
        
        Args:
            image_input: Uploaded image (numpy array or file path)
            
        Returns:
            Tuple of (result_image, prediction_info, disease_details)
        """
        try:
            if image_input is None:
                return None, "[ERROR] Please upload an image first", ""
            
            # Convert to PIL Image if numpy array
            if isinstance(image_input, np.ndarray):
                pil_image = Image.fromarray(image_input)
                # Save temporarily
                temp_path = os.path.join(tempfile.gettempdir(), f"temp_predict_{datetime.now().timestamp()}.jpg")
                pil_image.save(temp_path)
                image_to_predict = temp_path
            else:
                image_to_predict = image_input
                pil_image = Image.open(image_input)
            
            # Validate image
            if not validate_image_file(image_to_predict):
                return None, "[ERROR] Invalid image file. Please upload a valid image.", ""
            
            # Make prediction
            result = self.predictor.predict(pil_image, top_k=5)
            
            if not result['success']:
                return None, f"[ERROR] Prediction failed: {result['error']}", ""
            
            # Get prediction details
            top_pred = result['top_prediction']
            disease_class = top_pred['class']
            confidence = top_pred['confidence']
            
            # Get disease information
            disease_info = self.disease_db.get_disease_info(disease_class)
            
            # Format prediction info
            formatted_name = format_disease_name(disease_class)
            
            # Get emoji based on crop type
            crop_emoji = "🌿"
            if "Apple" in formatted_name:
                crop_emoji = "🍎"
            elif "Tomato" in formatted_name:
                crop_emoji = "🍅"
            elif "Corn" in formatted_name:
                crop_emoji = "🌽"
            elif "Grape" in formatted_name:
                crop_emoji = "🍇"
            elif "Potato" in formatted_name:
                crop_emoji = "🥔"
            elif "Orange" in formatted_name:
                crop_emoji = "🍊"

            # Determine risk level
            if confidence >= 90:
                risk_level = "HIGH"
                risk_color = "#ef4444"
            elif confidence >= 70:
                risk_level = "MEDIUM"
                risk_color = "#f97316"
            else:
                risk_level = "LOW"
                risk_color = "#22c55e"
            
            # Create confidence bar
            confidence_bar_length = int(confidence / 10)
            confidence_bar = "█" * confidence_bar_length + "░" * (10 - confidence_bar_length)
            
            # Get disease type and recommendation
            disease_type = "Unknown"
            recommendation = "Monitor closely."
            if disease_info:
                if "fungal" in disease_info['cause'].lower():
                    disease_type = "Fungal"
                elif "bacterial" in disease_info['cause'].lower():
                    disease_type = "Bacterial"
                elif "viral" in disease_info['cause'].lower():
                    disease_type = "Viral"
                
                if confidence >= 80:
                    recommendation = "Treat immediately."
                elif confidence >= 60:
                    recommendation = "Consider treatment."
                else:
                    recommendation = "Monitor and confirm."
            
            badge_class = "badge-blue"
            if risk_level == "HIGH":
                badge_class = "badge-red"
            elif risk_level == "MEDIUM":
                badge_class = "badge-orange"
            else:
                badge_class = "badge-green"

            confidence_percent = min(100, max(0, int(confidence)))
            confidence_width = max(8, min(100, confidence_percent))

            prediction_text = f"""
<div class="result-card">
  <div class="result-title">{crop_emoji} {formatted_name}</div>
  <div class="result-subtitle">Professional disease assessment summary</div>

  <div class="metric-row">
    <span class="metric-label">Confidence</span>
    <span class="metric-value">{confidence:.2f}%</span>
  </div>
  <div class="confidence-meter">
    <div class="confidence-fill" style="width: {confidence_width}%;"></div>
  </div>

  <div class="metric-row">
    <span class="metric-label">Risk</span>
    <span class="badge {badge_class}">{risk_level}</span>
  </div>

  <div class="metric-row">
    <span class="metric-label">Disease Type</span>
    <span class="badge badge-blue">{disease_type}</span>
  </div>

  <div class="metric-row">
    <span class="metric-label">Recommendation</span>
    <span class="metric-value">{recommendation}</span>
  </div>

  <div style="margin-top: 0.9rem; color: #cbd5e1; font-size: 0.92rem;"><strong>Top 5 Predictions</strong></div>
  <ul class="prediction-list">
"""
            for i, pred in enumerate(result['all_predictions'], 1):
                pred_name = format_disease_name(pred['class'])
                pred_conf = pred['confidence']
                prediction_text += f"""
    <li><span>{i}. {pred_name}</span><span class="value">{pred_conf:.2f}%</span></li>
"""
            prediction_text += """
  </ul>
</div>
"""
            
            # Format disease details
            if disease_info:
                disease_details = f"""
<div style="display: flex; flex-direction: column; gap: 0.4rem;">
  <div class="details-card">
    <h3>📋 Disease Details</h3>
    <p><strong>Name:</strong> {disease_info['name']}<br>
    <strong>Scientific Name:</strong> {disease_info['scientific_name']}<br>
    <strong>Difficulty:</strong> {disease_info['difficulty']}</p>
  </div>

  <div class="details-card">
    <h3>📝 Description</h3>
    <p>{disease_info['description']}</p>
  </div>

  <div class="details-card">
    <h3>🦠 Symptoms</h3>
    <p>{disease_info['symptoms']}</p>
  </div>

  <div class="details-card">
    <h3>⚠️ Cause</h3>
    <p>{disease_info['cause']}</p>
  </div>

  <div class="details-card">
    <h3>💊 Treatment Options</h3>
    <p><strong>Organic Treatment:</strong> {disease_info['treatment_organic']}<br><br>
    <strong>Chemical Treatment:</strong> {disease_info['treatment_chemical']}</p>
  </div>

  <div class="details-card">
    <h3>🛡️ Prevention</h3>
    <p>{disease_info['prevention']}</p>
  </div>
</div>
"""
            else:
                disease_details = "No detailed information available for this disease."
            
            # Save to database
            try:
                thumbnail_path = save_thumbnail(image_to_predict, "history")
                
                prediction_data = {
                    'image_path': image_to_predict,
                    'image_hash': None,
                    'disease_class': disease_class,
                    'disease_name': formatted_name,
                    'confidence': confidence,
                    'prediction_time': result['prediction_time'],
                    'top_predictions': result['all_predictions'],
                    'thumbnail_path': thumbnail_path
                }
                
                self.database.add_prediction(prediction_data)
            except Exception as e:
                print(f"[WARNING] Could not save to database: {e}")
            
            return pil_image, prediction_text, disease_details
            
        except Exception as e:
            error_msg = f"[ERROR] Error during prediction: {str(e)}"
            print(error_msg)
            return None, error_msg, ""
    
    def get_prediction_history(self):
        """Get prediction history for display"""
        try:
            predictions = self.database.get_all_predictions(limit=20)
            
            if not predictions:
                return "No prediction history yet. Upload an image to get started!"
            
            history_text = ""
            
            for pred in predictions:
                timestamp = format_timestamp(pred['timestamp'])
                disease_name = pred['disease_name']
                confidence = pred['confidence']
                
                # Get emoji for disease
                crop_emoji = "🌿"
                if "Apple" in disease_name:
                    crop_emoji = "🍎"
                elif "Tomato" in disease_name:
                    crop_emoji = "🍅"
                elif "Corn" in disease_name:
                    crop_emoji = "🌽"
                elif "Grape" in disease_name:
                    crop_emoji = "🍇"
                elif "Potato" in disease_name:
                    crop_emoji = "🥔"
                elif "Orange" in disease_name:
                    crop_emoji = "🍊"
                
                # Create confidence bar
                conf_bar_length = int(confidence / 10)
                conf_bar = "█" * conf_bar_length + "░" * (10 - conf_bar_length)
                
                history_text += f"""
<div class="history-entry">
  <div class="history-entry-header">
    <div class="history-entry-title">{crop_emoji} {disease_name}</div>
    <div class="history-entry-time">🕒 {timestamp}</div>
  </div>
  <div class="history-entry-meta">
    <span style="font-family: monospace; color: #818cf8;">{conf_bar}</span>
    <span style="margin-left: 0.45rem; color: #cbd5e1;">{confidence:.2f}%</span>
  </div>
  <div class="history-entry-actions">
    <a class="history-entry-btn" href="#">📄 View Report</a>
  </div>
</div>
"""
            
            if not history_text:
                return "No prediction history yet. Upload an image to get started!"
            
            return history_text
            
        except Exception as e:
            return f"[ERROR] Error loading history: {str(e)}"
    
    def clear_history(self):
        """Clear prediction history"""
        try:
            self.database.clear_all_predictions()
            return "[OK] History cleared successfully!"
        except Exception as e:
            return f"[ERROR] Error clearing history: {str(e)}"
    
    def generate_report(self, image_input):
        """Generate PDF report for prediction"""
        try:
            if image_input is None:
                return None, "[ERROR] Please upload an image first"
            
            # Get prediction
            result_image, prediction_text, disease_details = self.predict_image(image_input)
            
            if result_image is None:
                return None, prediction_text

            if isinstance(image_input, np.ndarray):
                pil_image = Image.fromarray(image_input)
                report_image_path = os.path.join(tempfile.gettempdir(), f"report_{datetime.now().timestamp()}.jpg")
                pil_image.save(report_image_path)
            else:
                report_image_path = image_input
                pil_image = Image.open(image_input)

            prediction_result = self.predictor.predict(pil_image, top_k=5)
            if not prediction_result['success']:
                return None, "[ERROR] Could not generate prediction details for report"

            top_prediction = prediction_result['top_prediction']
            disease_name = format_disease_name(top_prediction['class'])
            confidence = float(top_prediction['confidence'])
            disease_class = top_prediction['class']
            disease_info = self.disease_db.get_disease_info(disease_class)
            
            # Generate report filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            report_path = f"reports/PlantCure_Report_{timestamp}.pdf"
            
            # Prepare prediction data
            prediction_data = {
                'image_path': report_image_path,
                'disease_name': disease_name,
                'confidence': confidence,
                'prediction_time': prediction_result.get('prediction_time', 0.0),
                'top_predictions': prediction_result.get('all_predictions', [])
            }
            
            # Generate PDF
            if generate_pdf_report(prediction_data, disease_info, report_path):
                return report_path, f"[OK] Report generated: {report_path}"
            else:
                return None, "[ERROR] Failed to generate report"
                
        except Exception as e:
            return None, f"[ERROR] Error generating report: {str(e)}"
    
    def create_ui(self):
        """Create the Gradio UI"""
        
        # Refined styling for a tighter desktop-application look
        self.custom_css = """
        body {
            background: #060816;
        }

        .gradio-container {
            max-width: 1600px !important;
            width: min(100%, 1600px) !important;
            padding: 0.5rem 0.8rem !important;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
        }

        .app-shell {
            gap: 0.85rem;
            width: 100%;
        }

        .main-grid {
            gap: 0.85rem !important;
            align-items: stretch;
            justify-content: space-between;
            width: 100%;
        }

        .panel-column {
            display: flex;
            flex-direction: column;
            height: 100%;
            min-width: 0;
        }

        .panel-card {
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            height: 100%;
            min-height: 470px;
            width: 100%;
            background: rgba(255, 255, 255, 0.04);
            border-radius: 16px;
            padding: 0.8rem 0.9rem;
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 14px 32px rgba(2, 6, 23, 0.25);
        }

        .hero-section {
            text-align: center;
            padding: 0.9rem 1.2rem;
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.16) 0%, rgba(168, 85, 247, 0.16) 100%);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            box-shadow: 0 10px 30px rgba(2, 6, 23, 0.35);
            margin-bottom: 0.2rem;
        }

        .hero-title {
            color: #ffffff;
            font-size: 1.7rem;
            font-weight: 700;
            margin-bottom: 0.15rem;
        }

        .hero-subtitle {
            color: #cbd5e1;
            font-size: 0.95rem;
            margin: 0;
        }

        .main-grid {
            gap: 0.7rem !important;
            align-items: stretch;
        }

        .panel-column {
            display: flex;
            flex-direction: column;
            height: 100%;
        }

        .panel-card {
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            height: 100%;
            min-height: 470px;
            background: rgba(255, 255, 255, 0.04);
            border-radius: 16px;
            padding: 0.8rem 0.9rem;
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 14px 32px rgba(2, 6, 23, 0.25);
        }

        .section-title {
            color: #ffffff;
            font-size: 0.98rem;
            font-weight: 600;
            margin-bottom: 0.55rem;
            letter-spacing: 0.01em;
        }

        .glass-card {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 14px;
            padding: 0.9rem 1rem;
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: all 0.2s ease;
        }

        .glass-card:hover {
            background: rgba(255, 255, 255, 0.07);
            border-color: rgba(255, 255, 255, 0.15);
        }

        .btn-primary {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 0.7rem 1.1rem;
            border-radius: 12px;
            font-weight: 600;
            transition: all 0.2s ease;
        }

        .btn-primary:hover {
            transform: translateY(-1px);
            box-shadow: 0 6px 16px rgba(102, 126, 234, 0.35);
        }

        .btn-secondary {
            background: rgba(255, 255, 255, 0.08);
            color: white;
            border: 1px solid rgba(255, 255, 255, 0.15);
            padding: 0.7rem 1.1rem;
            border-radius: 12px;
            transition: all 0.2s ease;
        }

        .btn-secondary:hover {
            background: rgba(255, 255, 255, 0.12);
            transform: translateY(-1px);
        }

        .footer {
            text-align: center;
            padding: 1rem 0 0.25rem;
            color: #64748b;
            font-size: 0.82rem;
            margin-top: 0.25rem;
        }

        .confidence-bar-container {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 8px;
            height: 8px;
            overflow: hidden;
            margin: 0.4rem 0;
        }

        .confidence-bar-fill {
            height: 100%;
            background: linear-gradient(90deg, #667eea, #764ba2);
            border-radius: 8px;
            transition: width 0.5s ease;
        }

        .history-card {
            background: rgba(255, 255, 255, 0.03);
            border-radius: 12px;
            padding: 0.85rem 0.95rem;
            margin-bottom: 0.7rem;
            border: 1px solid rgba(255, 255, 255, 0.08);
            transition: all 0.2s ease;
        }

        .history-card:hover {
            background: rgba(255, 255, 255, 0.05);
            border-color: rgba(255, 255, 255, 0.15);
            transform: translateY(-1px);
        }

        .result-card {
            background: linear-gradient(135deg, rgba(15, 23, 42, 0.95), rgba(30, 41, 59, 0.9));
            border: 1px solid rgba(148, 163, 184, 0.18);
            border-radius: 18px;
            padding: 1rem 1.1rem;
            box-shadow: 0 12px 30px rgba(2, 6, 23, 0.28);
        }

        .result-title {
            font-size: 1.4rem;
            font-weight: 700;
            color: #f8fafc;
            margin: 0 0 0.35rem 0;
        }

        .result-subtitle {
            color: #cbd5e1;
            font-size: 0.95rem;
            margin-bottom: 0.8rem;
        }

        .metric-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 0.75rem;
            margin: 0.6rem 0;
        }

        .metric-label {
            color: #94a3b8;
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
        }

        .metric-value {
            color: #f8fafc;
            font-weight: 600;
        }

        .badge {
            display: inline-block;
            padding: 0.32rem 0.7rem;
            border-radius: 999px;
            font-size: 0.8rem;
            font-weight: 600;
            color: white;
        }

        .badge-blue {
            background: linear-gradient(135deg, #3b82f6, #2563eb);
        }

        .badge-orange {
            background: linear-gradient(135deg, #f59e0b, #ea580c);
        }

        .badge-green {
            background: linear-gradient(135deg, #22c55e, #16a34a);
        }

        .badge-red {
            background: linear-gradient(135deg, #ef4444, #dc2626);
        }

        .confidence-meter {
            width: 100%;
            height: 10px;
            border-radius: 999px;
            background: rgba(255, 255, 255, 0.12);
            overflow: hidden;
            margin-top: 0.35rem;
        }

        .confidence-fill {
            height: 100%;
            border-radius: 999px;
            background: linear-gradient(90deg, #22c55e 0%, #3b82f6 50%, #8b5cf6 100%);
        }

        .prediction-list {
            margin-top: 0.8rem;
            padding: 0;
            list-style: none;
        }

        .prediction-list li {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0.45rem 0;
            color: #e2e8f0;
            border-bottom: 1px solid rgba(255,255,255,0.08);
        }

        .prediction-list li:last-child {
            border-bottom: none;
        }

        .prediction-list .value {
            color: #cbd5e1;
            font-size: 0.9rem;
        }

        .details-card {
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 14px;
            padding: 0.9rem 1rem;
            margin-bottom: 0.8rem;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.03);
        }

        .details-card h3 {
            color: #f8fafc;
            font-size: 1rem;
            font-weight: 700;
            margin: 0 0 0.45rem 0;
        }

        .details-card p {
            color: #cbd5e1;
            line-height: 1.6;
            margin: 0;
            font-size: 0.93rem;
        }

        .details-card strong {
            color: #f8fafc;
        }

        .upload-shell {
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.12), rgba(168, 85, 247, 0.1));
            border: 1px dashed rgba(148, 163, 184, 0.35);
            border-radius: 16px;
            padding: 0.8rem;
        }

        .upload-shell .dropzone {
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 14px;
            background: rgba(15, 23, 42, 0.45);
            padding: 1rem;
            min-height: 220px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .upload-help {
            text-align: center;
            color: #cbd5e1;
            line-height: 1.6;
            font-size: 0.92rem;
            margin-top: 0.65rem;
        }

        .upload-help strong {
            color: #f8fafc;
        }

        .history-entry {
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.09);
            border-radius: 12px;
            padding: 0.75rem 0.85rem;
            margin-bottom: 0.7rem;
        }

        .history-entry-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 0.6rem;
            margin-bottom: 0.45rem;
        }

        .history-entry-time {
            color: #94a3b8;
            font-size: 0.78rem;
        }

        .history-entry-title {
            color: #f8fafc;
            font-size: 0.98rem;
            font-weight: 600;
        }

        .history-entry-meta {
            color: #cbd5e1;
            font-size: 0.9rem;
            margin-bottom: 0.4rem;
        }

        .history-entry-actions {
            margin-top: 0.35rem;
        }

        .history-entry-btn {
            display: inline-block;
            padding: 0.35rem 0.65rem;
            border-radius: 999px;
            background: rgba(99, 102, 241, 0.16);
            color: #c7d2fe;
            font-size: 0.8rem;
            font-weight: 600;
            text-decoration: none;
            border: 1px solid rgba(99, 102, 241, 0.25);
            transition: all 0.2s ease;
        }

        .history-entry-btn:hover {
            background: rgba(99, 102, 241, 0.24);
            transform: translateY(-1px);
        }

        .history-output {
            max-height: 220px;
            overflow-y: auto;
            padding-right: 0.2rem;
        }

        .gr-row {
            gap: 0.75rem !important;
        }

        .gr-column {
            gap: 0.6rem;
        }
        """
        
        # Create the interface
        with gr.Blocks() as app:
            
            with gr.Column(elem_classes="app-shell"):
                # Header
                gr.HTML("""
                <div class="hero-section">
                    <h1 class="hero-title">🌿 PlantCure.ai</h1>
                    <p class="hero-subtitle">AI-Powered Plant Disease Detection</p>
                </div>
                """)
                
                # Main content
                with gr.Row(elem_classes="main-grid"):
                    # Left column - Upload and predict
                    with gr.Column(scale=1, elem_classes="panel-column"):
                        with gr.Column(elem_classes="panel-card"):
                            gr.HTML('<div class="section-title">📤 Upload Image</div>')
                            
                            with gr.Group(elem_classes="upload-shell"):
                                gr.HTML("""
                                <div class="upload-help">
                                    <strong>Drop a healthy or infected plant image here</strong><br>
                                    JPG, PNG, or WEBP files are supported.<br>
                                    Clear lighting and a close-up leaf view improve results.
                                </div>
                                """)
                                image_input = gr.Image(
                                    label="Drag & Drop or Browse",
                                    sources=["upload"],
                                    type="numpy",
                                    height=260,
                                    elem_classes="dropzone"
                                )
                            
                            with gr.Row():
                                predict_btn = gr.Button("🔍 Predict Disease", size="lg", elem_classes="btn-primary")
                                clear_btn = gr.Button("🗑️ Clear", elem_classes="btn-secondary")
                            
                            gr.HTML('<div class="section-title">📸 Quick Tips</div>')
                            gr.HTML("""
                            <div class="glass-card">
                                <p style="color: #cbd5e1; line-height: 1.7; margin: 0;">
                                    ✨ Use clear, well-lit images<br>
                                    🎯 Focus on affected leaves<br>
                                    📷 Include multiple angles if possible<br>
                                    🔍 Ensure good resolution
                                </p>
                            </div>
                            """)
                    
                    # Right column - Results
                    with gr.Column(scale=1, elem_classes="panel-column"):
                        with gr.Column(elem_classes="panel-card"):
                            gr.HTML('<div class="section-title">🎯 Prediction Results</div>')
                            
                            with gr.Group(elem_classes="glass-card"):
                                result_image = gr.Image(label="", height=235)
                                
                                prediction_output = gr.HTML(label="")
                                disease_details = gr.HTML(label="")
                            
                            with gr.Row():
                                report_btn = gr.Button("📄 Generate PDF Report", elem_classes="btn-secondary")
                                download_output = gr.File(label="Download Report")
                
                # Bottom section - History
                with gr.Column(elem_classes="panel-card"):
                    gr.HTML('<div class="section-title">📜 Prediction History</div>')
                    
                    with gr.Group(elem_classes="glass-card"):
                        history_output = gr.HTML(elem_classes="history-output")
                        
                        with gr.Row():
                            refresh_btn = gr.Button("🔄 Refresh", elem_classes="btn-secondary")
                            clear_history_btn = gr.Button("🗑️ Clear History", elem_classes="btn-secondary")
                
                # Footer
                gr.HTML("""
                <div class="footer" style="padding: 0.6rem 0 0.25rem;">
                    <p style="margin: 0.2rem 0;">Built with ❤️ using TensorFlow, Gradio & Modern AI Technology</p>
                    <p style="margin: 0.2rem 0;">PlantCure.ai © 2024 - Hack Club Stardance Project</p>
                </div>
                """)
            
            # Event handlers
            predict_btn.click(
                fn=self.predict_image,
                inputs=[image_input],
                outputs=[result_image, prediction_output, disease_details]
            )
            
            clear_btn.click(
                fn=lambda: (None, "", ""),
                outputs=[image_input, prediction_output, disease_details]
            )
            
            report_btn.click(
                fn=self.generate_report,
                inputs=[image_input],
                outputs=[download_output, prediction_output]
            )
            
            refresh_btn.click(
                fn=self.get_prediction_history,
                outputs=[history_output]
            )
            
            clear_history_btn.click(
                fn=self.clear_history,
                outputs=[history_output]
            )
            
            # Load initial data
            app.load(
                fn=self.get_prediction_history,
                outputs=[history_output]
            )
        
        return app


def _override_uvicorn_default_log_config() -> None:
    """Override Uvicorn's default log config to avoid terminal-only formatters."""
    import uvicorn.config as uvicorn_config

    custom_log_config = copy.deepcopy(uvicorn_config.LOGGING_CONFIG)
    custom_log_config["formatters"]["default"] = {
        "class": "logging.Formatter",
        "fmt": "%(levelname)s: %(message)s",
    }
    custom_log_config["formatters"]["access"] = {
        "class": "logging.Formatter",
        "fmt": "%(levelname)s: %(message)s",
    }

    uvicorn_config.LOGGING_CONFIG.clear()
    uvicorn_config.LOGGING_CONFIG.update(custom_log_config)


def main():
    """Main function to run the application"""
    try:
        print("Starting PlantCure.ai...")
        
        # Initialize app
        app_instance = PlantCureApp()
        
        # Create UI
        app = app_instance.create_ui()
        
        # Launch app on an available local port
        print("Launching application...")
        preferred_port = int(os.environ.get("GRADIO_SERVER_PORT", "7860"))
        server_port = preferred_port
        for port in range(preferred_port, preferred_port + 10):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                try:
                    sock.bind(("127.0.0.1", port))
                    server_port = port
                    break
                except OSError:
                    continue

        _override_uvicorn_default_log_config()

        launch_kwargs = {
            "server_name": "127.0.0.1",
            "server_port": server_port,
            "share": False,
            "show_error": True,
            "quiet": False,
            "inbrowser": True,
            "css": app_instance.custom_css,
            "theme": gr.themes.Soft()
        }

        app.launch(**launch_kwargs)
        
    except Exception as e:
        print(f"[ERROR] Fatal error starting application: {e}")
        raise


if __name__ == "__main__":
    main()
