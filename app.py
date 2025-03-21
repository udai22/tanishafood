from flask import Flask, render_template, request, jsonify
import mesh
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_food():
    food = request.form.get('food')
    if not food:
        return jsonify({'error': 'Please enter what food you ate'}), 400
    
    # Create a detailed prompt for the mesh API
    prompt = f"""
    I just ate {food}. Please explain in detail:
    1. How this food is broken down in my body
    2. The biochemical and metabolic pathways that are activated
    3. How these pathways affect my body's systems
    4. Any positive or negative health impacts
    5. The specific nutrients, their roles, and how they're processed
    
    Please be scientifically accurate but explain complex terms.
    """
    
    # Get response from mesh
    response = mesh.chat(prompt)
    
    return jsonify({'response': response})

if __name__ == '__main__':
    # Use PORT environment variable for Render deployment, or 8080 for local development
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', debug=True, port=port)
