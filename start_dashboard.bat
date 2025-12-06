@echo off
REM Phone Addiction Dashboard - Quick Start Script (Windows)
REM This script sets up and runs the Streamlit dashboard

echo ==========================================
echo Phone Addiction Dashboard - Quick Setup
echo ==========================================
echo.

REM Check Python version
echo Checking Python version...
python --version

if errorlevel 1 (
    echo Error: Python is not installed. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

REM Create virtual environment (optional but recommended)
echo.
echo Creating virtual environment...
python -m venv venv

if %errorlevel% equ 0 (
    echo Virtual environment created successfully!
    
    REM Activate virtual environment
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
) else (
    echo Warning: Could not create virtual environment. Continuing with global Python...
)

REM Install dependencies
echo.
echo Installing required packages...
pip install -r requirements.txt

if errorlevel 1 (
    echo Error: Failed to install dependencies. Please check your internet connection.
    pause
    exit /b 1
)

echo.
echo ==========================================
echo Setup complete! Starting dashboard...
echo ==========================================
echo.
echo The dashboard will open in your browser automatically.
echo If it doesn't, navigate to: http://localhost:8501
echo.
echo Press Ctrl+C to stop the dashboard.
echo.

REM Run Streamlit
streamlit run phone_addiction_dashboard.py

pause
