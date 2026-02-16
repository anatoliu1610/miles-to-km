"""
Miles to Kilometers Converter
A simple Flask web app with API and HTML frontend.
"""

from flask import Flask, request, jsonify, render_template_string
import os

app = Flask(__name__)

# HTML frontend (inline for simplicity)
HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Miles to Kilometers</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; max-width: 600px; margin: 40px auto; padding: 20px; }
        input { width: 100%; padding: 12px; font-size: 18px; border: 2px solid #ddd; border-radius: 8px; box-sizing: border-box; margin-bottom: 10px; }
        button { background: #007bff; color: white; border: none; padding: 12px 24px; font-size: 18px; border-radius: 8px; cursor: pointer; width: 100%; }
        button:hover { background: #0056b3; }
        #result { margin-top: 20px; font-size: 24px; color: #333; padding: 15px; background: #f8f9fa; border-radius: 8px; }
        .error { color: #dc3545; background: #f8d7da; }
        .success { color: #155724; background: #d4edda; }
        a { color: #007bff; }
    </style>
</head>
<body>
    <h1>Miles → Kilometers</h1>
    <p>Enter distance in miles to convert to kilometers.</p>
    <input id="miles" type="number" step="any" placeholder="e.g. 10" min="0">
    <button onclick="convert()">Convert</button>
    <div id="result"></div>
    <p><small>Conversion factor: 1 mile = 1.60934 km</small></p>

    <script>
        async function convert() {
            const miles = parseFloat(document.getElementById('miles').value);
            const resultDiv = document.getElementById('result');
            
            if (isNaN(miles) || miles < 0) {
                resultDiv.className = 'error';
                resultDiv.textContent = 'Please enter a valid positive number';
                return;
            }
            
            try {
                const response = await fetch('/convert', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ miles: miles })
                });
                
                const data = await response.json();
                
                if (response.ok) {
                    resultDiv.className = 'success';
                    resultDiv.textContent = `${miles} mile(s) = ${data.kilometers.toFixed(4)} km`;
                } else {
                    resultDiv.className = 'error';
                    resultDiv.textContent = 'Error: ' + (data.error || 'Unknown error');
                }
            } catch (e) {
                resultDiv.className = 'error';
                resultDiv.textContent = 'Network error. Please try again.';
            }
        }
        
        // Allow Enter key to submit
        document.getElementById('miles').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') convert();
        });
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint for deployment platforms."""
    return jsonify(status='healthy', service='miles-to-km')

@app.route('/convert', methods=['POST'])
def convert():
    """API endpoint: convert miles to kilometers."""
    data = request.json
    
    if not data:
        return jsonify(error='Missing JSON body'), 400
    
    miles = data.get('miles')
    
    if miles is None:
        return jsonify(error='Missing "miles" field'), 400
    
    try:
        miles = float(miles)
    except (ValueError, TypeError):
        return jsonify(error='"miles" must be a number'), 400
    
    if miles < 0:
        return jsonify(error='Miles cannot be negative'), 400
    
    # Conversion: 1 mile = 1.60934 km
    kilometers = miles * 1.60934
    
    return jsonify(
        miles=miles,
        kilometers=round(kilometers, 4),
        unit='km'
    )

@app.errorhandler(404)
def not_found(e):
    return jsonify(error='Not found'), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify(error='Internal server error'), 500

if __name__ == '__main__':
    # For development
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug)