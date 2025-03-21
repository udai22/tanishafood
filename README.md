# Food Metabolism Analyzer

This Flask web application helps you understand the biochemical and metabolic pathways that are activated when you eat different foods. Simply enter what food you ate, and the application will provide a detailed analysis of how your body processes it.

## Features

- Simple, user-friendly interface
- Detailed analysis of food metabolism
- Information about biochemical and metabolic pathways
- Explanations of how nutrients are processed
- Analysis of both healthy and unhealthy food choices

## Setup and Installation

1. Make sure you have Python 3.x installed
2. Create a virtual environment (optional but recommended):
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

1. Activate the virtual environment (if not already activated):
   ```
   source venv/bin/activate
   ```
2. Run the Flask application:
   ```
   python app.py
   ```
3. Open your web browser and navigate to `http://127.0.0.1:5000/`

## Usage

1. Enter the food you recently ate in the input field
2. Click the "Analyze Metabolism" button
3. View the detailed analysis of how your body processes the food

## Technologies Used

- Flask - Web framework
- Mesh SDK - For AI-powered analysis
- Bootstrap - For the user interface
