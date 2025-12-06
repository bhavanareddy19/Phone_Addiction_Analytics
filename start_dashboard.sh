#!/bin/bash

# Phone Addiction Dashboard - Quick Start Script
# This script sets up and runs the Streamlit dashboard

echo "=========================================="
echo "Phone Addiction Dashboard - Quick Setup"
echo "=========================================="
echo ""

# Check Python version
echo "Checking Python version..."
python3 --version

if [ $? -ne 0 ]; then
    echo "Error: Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Create virtual environment (optional but recommended)
echo ""
echo "Creating virtual environment..."
python3 -m venv venv

if [ $? -eq 0 ]; then
    echo "Virtual environment created successfully!"
    
    # Activate virtual environment
    echo "Activating virtual environment..."
    source venv/bin/activate
else
    echo "Warning: Could not create virtual environment. Continuing with global Python..."
fi

# Install dependencies
echo ""
echo "Installing required packages..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "Error: Failed to install dependencies. Please check your internet connection."
    exit 1
fi

echo ""
echo "=========================================="
echo "Setup complete! Starting dashboard..."
echo "=========================================="
echo ""
echo "The dashboard will open in your browser automatically."
echo "If it doesn't, navigate to: http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the dashboard."
echo ""

# Run Streamlit
streamlit run phone_addiction_dashboard.py
