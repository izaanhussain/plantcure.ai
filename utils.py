"""
Utility Functions for PlantCure.ai
Helper functions for image processing, PDF generation, and formatting
"""

import os
import sys
import io
from datetime import datetime
from PIL import Image
import hashlib


def _is_pyinstaller_bundle():
    return getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS")


def resource_path(relative_path):
    """Resolve resource paths for development and PyInstaller execution."""
    if os.path.isabs(relative_path):
        return relative_path

    base_path = sys._MEIPASS if _is_pyinstaller_bundle() else os.path.dirname(os.path.abspath(__file__))
    return os.path.abspath(os.path.join(base_path, relative_path))


def get_user_data_dir():
    """Return a writable directory for app data on the current machine."""
    if os.name == "nt":
        local_appdata = os.environ.get("LOCALAPPDATA")
        if local_appdata:
            base_dir = os.path.join(local_appdata, "PlantCure.ai")
        else:
            base_dir = os.path.expanduser(r"~\AppData\Local\PlantCure.ai")
    else:
        base_dir = os.path.expanduser("~/.plantcure")

    os.makedirs(base_dir, exist_ok=True)
    return base_dir


def get_writable_data_dir(folder_name):
    """Return a writable folder for application data such as history or reports."""
    folder_path = os.path.join(get_user_data_dir(), folder_name)
    os.makedirs(folder_path, exist_ok=True)
    return folder_path


def create_directories():
    """Create necessary writable directories for the application."""
    for directory in ['history', 'reports']:
        os.makedirs(get_writable_data_dir(directory), exist_ok=True)


def save_thumbnail(image_path, target_dir, size=(200, 200)):
    """
    Save a thumbnail of the image
    
    Args:
        image_path: Path to the original image
        target_dir: Directory to save thumbnail
        size: Thumbnail size (width, height)
        
    Returns:
        Path to the saved thumbnail
    """
    try:
        resolved_dir = target_dir
        if not os.path.isabs(resolved_dir):
            resolved_dir = get_writable_data_dir(target_dir)
        else:
            os.makedirs(resolved_dir, exist_ok=True)
        
        # Generate unique filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        hash_val = hashlib.md5(str(image_path).encode()).hexdigest()[:8]
        thumbnail_name = f"thumb_{timestamp}_{hash_val}.jpg"
        thumbnail_path = os.path.join(resolved_dir, thumbnail_name)
        
        # Open and resize image
        img = Image.open(image_path)
        img.thumbnail(size)
        img.save(thumbnail_path, "JPEG", quality=85)
        
        return thumbnail_path
    except Exception:
        return None


def format_disease_name(disease_class):
    """
    Format disease class name for display
    
    Args:
        disease_class: Raw disease class name (e.g., 'Tomato___Early_blight')
        
    Returns:
        Formatted name (e.g., 'Tomato Early Blight')
    """
    return disease_class.replace('___', ' ').replace('_', ' ')


def get_confidence_color(confidence):
    """
    Get color based on confidence level
    
    Args:
        confidence: Confidence percentage (0-100)
        
    Returns:
        Color code string
    """
    if confidence >= 80:
        return "#22c55e"
    elif confidence >= 60:
        return "#eab308"
    elif confidence >= 40:
        return "#f97316"
    else:
        return "#ef4444"


def validate_image_file(image_path):
    """
    Validate if file is a valid image
    
    Args:
        image_path: Path to the image file
        
    Returns:
        True if valid image, False otherwise
    """
    try:
        if not os.path.exists(image_path):
            return False
        
        # Check file extension
        valid_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.webp']
        ext = os.path.splitext(image_path)[1].lower()
        if ext not in valid_extensions:
            return False
        
        # Try to open with PIL
        with Image.open(image_path) as img:
            img.verify()
        
        return True
    except Exception:
        return False


def format_timestamp(timestamp_str):
    """
    Format timestamp for display
    
    Args:
        timestamp_str: ISO format timestamp string
        
    Returns:
        Formatted timestamp string
    """
    try:
        dt = datetime.fromisoformat(timestamp_str)
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        try:
            dt = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
            return dt.strftime("%Y-%m-%d %H:%M:%S")
        except Exception:
            return timestamp_str


def generate_pdf_report(prediction_data, disease_info, report_path):
    """
    Generate PDF report for prediction using ReportLab.
    """
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as ReportImage
        from reportlab.lib import colors
        from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
        from reportlab.lib.utils import ImageReader
        from reportlab.graphics.shapes import Drawing, Circle, String, Rect

        doc = SimpleDocTemplate(report_path, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []

        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Title'],
            fontName='Helvetica-Bold',
            fontSize=20,
            textColor=colors.HexColor('#0f172a'),
            spaceAfter=0.08 * inch,
        )
        subtitle_style = ParagraphStyle(
            'CustomSubtitle',
            parent=styles['Normal'],
            fontName='Helvetica',
            fontSize=10,
            textColor=colors.HexColor('#64748b'),
            spaceAfter=0.12 * inch,
        )
        heading_style = ParagraphStyle(
            'SectionHeading',
            parent=styles['Heading2'],
            fontName='Helvetica-Bold',
            fontSize=12,
            textColor=colors.HexColor('#1d4ed8'),
            spaceBefore=0.12 * inch,
            spaceAfter=0.05 * inch,
        )
        body_style = ParagraphStyle(
            'BodyText',
            parent=styles['Normal'],
            fontName='Helvetica',
            fontSize=10,
            textColor=colors.HexColor('#334155'),
            leading=14,
            alignment=TA_JUSTIFY,
        )
        small_style = ParagraphStyle(
            'SmallText',
            parent=styles['Normal'],
            fontName='Helvetica',
            fontSize=9,
            textColor=colors.HexColor('#64748b'),
            leading=12,
        )

        def clean_text(value, fallback='Not available'):
            if value is None:
                return fallback
            text = str(value).replace('\n', '<br/>').strip()
            return text if text else fallback

        logo = Drawing(54, 40)
        logo.add(Rect(0, 6, 40, 28, fillColor=colors.HexColor('#22c55e'), strokeColor=colors.HexColor('#16a34a'), radius=8))
        logo.add(String(20, 20, 'P', fontName='Helvetica-Bold', fontSize=18, fillColor=colors.white, textAnchor='middle'))

        header_table = Table(
            [[logo, Paragraph('PlantCure.ai', title_style), Paragraph('Disease Report', subtitle_style)]],
            colWidths=[0.9 * inch, 2.8 * inch, 1.4 * inch],
            style=[('VALIGN', (0, 0), (-1, -1), 'MIDDLE')]
        )
        story.append(header_table)
        story.append(Spacer(1, 0.1 * inch))

        disease_name = clean_text(disease_info.get('name') if disease_info else prediction_data.get('disease_name'))
        scientific_name = clean_text(disease_info.get('scientific_name') if disease_info else '')
        confidence = float(prediction_data.get('confidence', 0) or 0)
        confidence_text = f"{confidence:.2f}%"

        summary_table = Table(
            [
                [Paragraph('<b>Disease</b>', body_style), Paragraph(disease_name, body_style)],
                [Paragraph('<b>Scientific Name</b>', body_style), Paragraph(scientific_name, body_style)],
                [Paragraph('<b>Confidence</b>', body_style), Paragraph(confidence_text, body_style)],
            ],
            colWidths=[1.4 * inch, 4.6 * inch],
            repeatRows=1,
        )
        summary_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f8fafc')),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#e2e8f0')),
            ('PADDING', (0, 0), (-1, -1), 6),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]))
        story.append(summary_table)
        story.append(Spacer(1, 0.2 * inch))

        image_path = prediction_data.get('image_path')
        if image_path and os.path.exists(image_path):
            try:
                with Image.open(image_path) as img:
                    img = img.convert('RGB')
                    img_bytes = io.BytesIO()
                    img.save(img_bytes, format='JPEG', quality=90)
                    img_bytes.seek(0)
                    report_image = ReportImage(ImageReader(img_bytes), width=2.8 * inch, height=2.2 * inch)
                    story.append(Paragraph('<b>Uploaded Image</b>', heading_style))
                    story.append(report_image)
                    story.append(Spacer(1, 0.15 * inch))
            except Exception:
                pass

        story.append(Paragraph('<b>Prediction Confidence</b>', heading_style))
        bar_width = max(0.2 * inch, min(4.4 * inch, (confidence / 100.0) * 4.4 * inch))
        confidence_draw = Drawing(4.4 * inch, 0.16 * inch)
        confidence_draw.add(Rect(0, 0, 4.4 * inch, 0.16 * inch, fillColor=colors.HexColor('#e2e8f0'), strokeColor=colors.HexColor('#cbd5e1')))
        confidence_draw.add(Rect(0, 0, bar_width, 0.16 * inch, fillColor=colors.HexColor('#22c55e'), strokeColor=colors.HexColor('#16a34a')))
        story.append(confidence_draw)
        story.append(Spacer(1, 0.08 * inch))
        story.append(Paragraph(f"Confidence level: {confidence_text}", body_style))
        story.append(Spacer(1, 0.16 * inch))

        story.append(Paragraph('<b>Top 5 Predictions</b>', heading_style))
        top_predictions = prediction_data.get('top_predictions', []) or []
        table_rows = [['#', 'Prediction', 'Confidence']]
        for index, pred in enumerate(top_predictions[:5], start=1):
            prediction_name = clean_text(pred.get('class'))
            confidence_value = float(pred.get('confidence', 0) or 0)
            table_rows.append([str(index), prediction_name, f"{confidence_value:.2f}%"])

        predictions_table = Table(table_rows, colWidths=[0.5 * inch, 3.2 * inch, 1.2 * inch])
        predictions_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1d4ed8')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e1')),
            ('PADDING', (0, 0), (-1, -1), 6),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]))
        story.append(predictions_table)
        story.append(Spacer(1, 0.2 * inch))

        story.append(Paragraph('<b>Description</b>', heading_style))
        story.append(Paragraph(clean_text(disease_info.get('description') if disease_info else ''), body_style))
        story.append(Spacer(1, 0.08 * inch))

        story.append(Paragraph('<b>Symptoms</b>', heading_style))
        story.append(Paragraph(clean_text(disease_info.get('symptoms') if disease_info else ''), body_style))
        story.append(Spacer(1, 0.08 * inch))

        story.append(Paragraph('<b>Cause</b>', heading_style))
        story.append(Paragraph(clean_text(disease_info.get('cause') if disease_info else ''), body_style))
        story.append(Spacer(1, 0.08 * inch))

        story.append(Paragraph('<b>Treatment Options</b>', heading_style))
        story.append(Paragraph(f"<b>Organic:</b> {clean_text(disease_info.get('treatment_organic') if disease_info else '')}", body_style))
        story.append(Spacer(1, 0.04 * inch))
        story.append(Paragraph(f"<b>Chemical:</b> {clean_text(disease_info.get('treatment_chemical') if disease_info else '')}", body_style))
        story.append(Spacer(1, 0.08 * inch))

        story.append(Paragraph('<b>Prevention</b>', heading_style))
        story.append(Paragraph(clean_text(disease_info.get('prevention') if disease_info else ''), body_style))
        story.append(Spacer(1, 0.2 * inch))

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        story.append(Paragraph(f'Generated by PlantCure.ai on {timestamp}', small_style))

        doc.build(story)
        return True
    except Exception:
        return False
