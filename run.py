#!/usr/bin/env python3

import sys
import subprocess
import os

def install_requirements():
    """Install required packages"""
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("✅ Dependencies installed successfully!")
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        return False
    return True

def run_app():
    """Run the Flask application"""
    try:
        from app import app
        print("🚀 Starting Flask Chess Game...")
        print("📝 Open your browser and go to: http://localhost:5000")
        app.run(debug=True, host='0.0.0.0', port=5000)
    except ImportError:
        print("❌ Failed to import Flask app. Make sure dependencies are installed.")
        return False

if __name__ == '__main__':
    print("🏁 Flask Chess Game Setup")
    print("=" * 40)
    
    if not os.path.exists('requirements.txt'):
        print("❌ requirements.txt not found!")
        sys.exit(1)
    
    if '--install' in sys.argv or not os.path.exists('venv'):
        print("📦 Installing dependencies...")
        if not install_requirements():
            sys.exit(1)
    
    print("🎮 Starting chess game...")
    run_app()