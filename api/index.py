"""
WSGI application untuk Vercel serverless functions
"""
import os
import sys

# Tambahkan project root ke Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app

# Create Flask app instance
app = create_app(os.getenv('FLASK_ENV', 'production'))
