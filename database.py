"""
Database Module
Handles SQLite database for prediction history
"""

import sqlite3
import os
import json
from datetime import datetime
import shutil


class PredictionDatabase:
    """Handles prediction history storage and retrieval"""
    
    def __init__(self, db_path=None):
        """
        Initialize database connection
        
        Args:
            db_path: Path to SQLite database file
        """
        self.db_path = db_path or "history/predictions.db"
        self.history_dir = os.path.dirname(self.db_path)
        
        # Ensure history directory exists
        if self.history_dir and not os.path.exists(self.history_dir):
            os.makedirs(self.history_dir)
        
        self._init_database()
    
    def _init_database(self):
        """Initialize database schema"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS predictions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    image_path TEXT,
                    image_hash TEXT,
                    disease_class TEXT NOT NULL,
                    disease_name TEXT NOT NULL,
                    confidence REAL NOT NULL,
                    prediction_time REAL NOT NULL,
                    top_predictions TEXT,
                    thumbnail_path TEXT
                )
            ''')
            
            conn.commit()
            conn.close()
            print(f"[OK] Database initialized at {self.db_path}")
            
        except Exception as e:
            print(f"[ERROR] Error initializing database: {e}")
            raise
    
    def add_prediction(self, prediction_data):
        """
        Add a prediction to the database
        
        Args:
            prediction_data: Dictionary containing prediction information
                - image_path: Path to original image
                - image_hash: Hash of image for deduplication
                - disease_class: Predicted disease class
                - disease_name: Human-readable disease name
                - confidence: Confidence percentage
                - prediction_time: Time taken for prediction
                - top_predictions: JSON string of all predictions
                - thumbnail_path: Path to saved thumbnail
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            timestamp = datetime.now().isoformat()
            
            cursor.execute('''
                INSERT INTO predictions 
                (timestamp, image_path, image_hash, disease_class, disease_name, 
                 confidence, prediction_time, top_predictions, thumbnail_path)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                timestamp,
                prediction_data.get('image_path'),
                prediction_data.get('image_hash'),
                prediction_data.get('disease_class'),
                prediction_data.get('disease_name'),
                prediction_data.get('confidence'),
                prediction_data.get('prediction_time'),
                json.dumps(prediction_data.get('top_predictions', [])),
                prediction_data.get('thumbnail_path')
            ))
            
            conn.commit()
            prediction_id = cursor.lastrowid
            conn.close()
            
            print(f"[OK] Prediction saved to database (ID: {prediction_id})")
            return prediction_id
            
        except Exception as e:
            print(f"[ERROR] Error adding prediction to database: {e}")
            return None
    
    def get_all_predictions(self, limit=None, offset=0):
        """
        Get all predictions from database
        
        Args:
            limit: Maximum number of predictions to return
            offset: Number of predictions to skip
            
        Returns:
            List of prediction dictionaries
        """
        try:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            query = 'SELECT * FROM predictions ORDER BY timestamp DESC'
            if limit:
                query += f' LIMIT {limit} OFFSET {offset}'
            
            cursor.execute(query)
            rows = cursor.fetchall()
            
            predictions = []
            for row in rows:
                prediction = dict(row)
                prediction['top_predictions'] = json.loads(prediction['top_predictions'])
                predictions.append(prediction)
            
            conn.close()
            return predictions
            
        except Exception as e:
            print(f"[ERROR] Error retrieving predictions: {e}")
            return []
    
    def get_prediction_by_id(self, prediction_id):
        """
        Get a specific prediction by ID
        
        Args:
            prediction_id: ID of the prediction
            
        Returns:
            Prediction dictionary or None
        """
        try:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM predictions WHERE id = ?', (prediction_id,))
            row = cursor.fetchone()
            
            if row:
                prediction = dict(row)
                prediction['top_predictions'] = json.loads(prediction['top_predictions'])
                conn.close()
                return prediction
            
            conn.close()
            return None
            
        except Exception as e:
            print(f"[ERROR] Error retrieving prediction: {e}")
            return None
    
    def delete_prediction(self, prediction_id):
        """
        Delete a prediction from database
        
        Args:
            prediction_id: ID of the prediction to delete
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Get thumbnail path before deleting
            cursor.execute('SELECT thumbnail_path FROM predictions WHERE id = ?', (prediction_id,))
            row = cursor.fetchone()
            
            # Delete from database
            cursor.execute('DELETE FROM predictions WHERE id = ?', (prediction_id,))
            conn.commit()
            conn.close()
            
            # Delete thumbnail file if exists
            if row and row[0] and os.path.exists(row[0]):
                try:
                    os.remove(row[0])
                    print(f"[OK] Deleted thumbnail: {row[0]}")
                except Exception as e:
                    print(f"[WARNING] Could not delete thumbnail: {e}")
            
            print(f"[OK] Prediction {prediction_id} deleted")
            
        except Exception as e:
            print(f"[ERROR] Error deleting prediction: {e}")
    
    def clear_all_predictions(self):
        """Delete all predictions from database and thumbnails"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Get all thumbnail paths
            cursor.execute('SELECT thumbnail_path FROM predictions')
            rows = cursor.fetchall()
            
            # Delete all predictions
            cursor.execute('DELETE FROM predictions')
            conn.commit()
            conn.close()
            
            # Delete all thumbnail files
            for row in rows:
                if row[0] and os.path.exists(row[0]):
                    try:
                        os.remove(row[0])
                    except Exception as e:
                        print(f"[WARNING] Could not delete thumbnail: {e}")
            
            print("[OK] All predictions cleared")
            
        except Exception as e:
            print(f"[ERROR] Error clearing predictions: {e}")
    
    def get_statistics(self):
        """Get database statistics"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Total predictions
            cursor.execute('SELECT COUNT(*) FROM predictions')
            total = cursor.fetchone()[0]
            
            # Most common diseases
            cursor.execute('''
                SELECT disease_name, COUNT(*) as count 
                FROM predictions 
                GROUP BY disease_name 
                ORDER BY count DESC 
                LIMIT 5
            ''')
            top_diseases = cursor.fetchall()
            
            # Average confidence
            cursor.execute('SELECT AVG(confidence) FROM predictions')
            avg_confidence = cursor.fetchone()[0] or 0
            
            conn.close()
            
            return {
                'total_predictions': total,
                'top_diseases': [{'name': row[0], 'count': row[1]} for row in top_diseases],
                'average_confidence': round(avg_confidence, 2)
            }
            
        except Exception as e:
            print(f"[ERROR] Error getting statistics: {e}")
            return {
                'total_predictions': 0,
                'top_diseases': [],
                'average_confidence': 0
            }
    
    def search_predictions(self, search_term, limit=None):
        """
        Search predictions by disease name
        
        Args:
            search_term: Search term
            limit: Maximum number of results
            
        Returns:
            List of matching predictions
        """
        try:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            query = '''
                SELECT * FROM predictions 
                WHERE disease_name LIKE ? OR disease_class LIKE ?
                ORDER BY timestamp DESC
            '''
            if limit:
                query += f' LIMIT {limit}'
            
            search_pattern = f'%{search_term}%'
            cursor.execute(query, (search_pattern, search_pattern))
            rows = cursor.fetchall()
            
            predictions = []
            for row in rows:
                prediction = dict(row)
                prediction['top_predictions'] = json.loads(prediction['top_predictions'])
                predictions.append(prediction)
            
            conn.close()
            return predictions
            
        except Exception as e:
            print(f"[ERROR] Error searching predictions: {e}")
            return []
    
    def export_to_json(self, export_path):
        """
        Export all predictions to JSON file
        
        Args:
            export_path: Path to export JSON file
        """
        try:
            predictions = self.get_all_predictions()
            
            with open(export_path, 'w') as f:
                json.dump(predictions, f, indent=2)
            
            print(f"[OK] Exported {len(predictions)} predictions to {export_path}")
            return True
            
        except Exception as e:
            print(f"[ERROR] Error exporting predictions: {e}")
            return False
    
    def get_prediction_count(self):
        """Get total number of predictions"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('SELECT COUNT(*) FROM predictions')
            count = cursor.fetchone()[0]
            conn.close()
            return count
        except Exception as e:
            print(f"[ERROR] Error getting prediction count: {e}")
            return 0


# Singleton instance for app-wide use
_db_instance = None


def get_database():
    """Get or create singleton database instance"""
    global _db_instance
    if _db_instance is None:
        _db_instance = PredictionDatabase()
    return _db_instance
