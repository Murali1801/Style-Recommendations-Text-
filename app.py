from flask import Flask, request, jsonify
from recommendation_system import get_recommendations
import json

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No input data provided'}), 400
    
    # Check for gender field if present
    if 'gender' in data and data['gender'].lower() != 'male':
        return jsonify({'error': 'This API currently only supports recommendations for men.'}), 400
    
    # Get recommendations from the recommendation system
    result = get_recommendations(data)
    
    if result['status'] == 'success':
        response = {
            "status": "success",
            "data": json.dumps(result['data'], indent=2)
        }
        return jsonify(response)
    else:
        return jsonify({'error': result['error']}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 