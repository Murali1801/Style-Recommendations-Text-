from flask import Flask, request, jsonify
from recommendation_system import get_recommendations
import json
import os

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No input data provided'}), 400
    
    # Check if gender is provided and is valid
    gender = data.get('gender', 'male')
    if gender.lower() not in ['male', 'female']:
        return jsonify({'error': 'Gender must be either "male" or "female"'}), 400
    
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

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({
        "status": "success",
        "message": "Fashion Recommendation API is running!",
        "endpoints": {
            "POST /recommend": "Get fashion recommendations based on measurements"
        }
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 