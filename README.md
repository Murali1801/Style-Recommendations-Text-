# Fashion Recommendation System

A personalized fashion recommendation system that provides style advice based on body measurements, designed for both men's and women's fashion.

## Features

- **Gender-specific recommendations**: Supports both male and female fashion advice
- **Height-based categorization**: 
  - **Men**: Short (160-166 cm), Average (175-182 cm), Tall (183+ cm)
  - **Women**: Petite (155-162 cm), Average (163-170 cm), Tall (171+ cm)
- **Personalized recommendations**: Provides specific advice for tops, bottoms, shoes, accessories, and color combinations
- **Search engine queries**: Generates optimized search queries for finding recommended clothing items
- **RESTful API**: Simple HTTP API for easy integration
- **JSON responses**: Structured responses for easy parsing and integration

## Project Structure

```
├── app.py                    # Flask API server
├── recommendation_system.py  # Core recommendation logic
└── README.md                # This file
```

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- Flask

### Installation

1. **Clone or download the project files**

2. **Install Flask** (if not already installed):
   ```bash
   pip install flask
   ```

3. **Run the API server**:
   ```bash
   python app.py
   ```

The server will start on `http://localhost:5000`

## API Documentation

### Endpoint: `/recommend`

**Method**: POST  
**Content-Type**: application/json

### Request Body

#### For Men:
```json
{
  "subject-height": 170.18,
  "subject-shoulder": 43.18,
  "subject-chest": 86.36,
  "subject-waist": 66.04,
  "subject-hip": 96.52,
  "subject-arm": 54.61,
  "subject-leg": 95.5,
  "gender": "male"
}
```

#### For Women:
```json
{
  "subject-height": 160.0,
  "subject-shoulder": 38.0,
  "subject-chest": 85.0,
  "subject-waist": 65.0,
  "subject-hip": 90.0,
  "subject-arm": 50.0,
  "subject-leg": 85.0,
  "gender": "female"
}
```

**Required Fields**:
- `subject-height`: Height in centimeters (used for categorization)
- `gender`: Must be either "male" or "female"

**Optional Fields**:
- Other measurement fields are optional but recommended for future enhancements

### Response Format

```json
{
  "status": "success",
  "data": {
    "text_recommendations": "Detailed analysis and recommendations...",
    "top_wear_search_engine_query": "henley shirts for men",
    "bottom_wear_search_engine_query": "chinos for tall men",
    "shoes_search_engine_query": "lace up brogues for men",
    "color_recommendations_search_engine_query": "smart casual color combinations for men"
  }
}
```

### Example Usage

#### Using cURL (Male)
```bash
curl -X POST http://localhost:5000/recommend \
  -H "Content-Type: application/json" \
  -d '{
    "subject-height": 170.18,
    "subject-shoulder": 43.18,
    "subject-chest": 86.36,
    "subject-waist": 66.04,
    "subject-hip": 96.52,
    "subject-arm": 54.61,
    "subject-leg": 95.5,
    "gender": "male"
  }'
```

#### Using cURL (Female)
```bash
curl -X POST http://localhost:5000/recommend \
  -H "Content-Type: application/json" \
  -d '{
    "subject-height": 160.0,
    "subject-shoulder": 38.0,
    "subject-chest": 85.0,
    "subject-waist": 65.0,
    "subject-hip": 90.0,
    "subject-arm": 50.0,
    "subject-leg": 85.0,
    "gender": "female"
  }'
```

#### Using Python requests
```python
import requests

# Male example
male_data = {
    "subject-height": 170.18,
    "subject-shoulder": 43.18,
    "subject-chest": 86.36,
    "subject-waist": 66.04,
    "subject-hip": 96.52,
    "subject-arm": 54.61,
    "subject-leg": 95.5,
    "gender": "male"
}

# Female example
female_data = {
    "subject-height": 160.0,
    "subject-shoulder": 38.0,
    "subject-chest": 85.0,
    "subject-waist": 65.0,
    "subject-hip": 90.0,
    "subject-arm": 50.0,
    "subject-leg": 85.0,
    "gender": "female"
}

response = requests.post('http://localhost:5000/recommend', json=male_data)
print(response.json())
```

## Height Categories and Recommendations

### Men's Categories

#### Short (160-166 cm)
- **Tops**: Vertical stripes, structured fits, shorter-length jackets
- **Bottoms**: Slim/skinny jeans, cropped trousers
- **Shoes**: Chelsea boots, low profile sneakers
- **Accessories**: Narrow belts, minimal backpacks
- **Colors**: Monochrome dressing, darker shades

#### Average (175-182 cm)
- **Tops**: Button-up shirts, Henleys, layered jackets
- **Bottoms**: Chinos, slim jeans, cargo pants
- **Shoes**: Brogues, classic sneakers, high-tops
- **Accessories**: Long scarves, satchels, messenger bags
- **Colors**: Mix of bold and muted tones

#### Tall (183+ cm)
- **Tops**: Longline jackets, oversized shirts, layered hoodies
- **Bottoms**: Relaxed-fit trousers, high-waisted pants
- **Shoes**: Chunky sneakers, boots
- **Accessories**: Wide leather bands, tall backpacks
- **Colors**: Contrasts, layered neutrals with bold accents

### Women's Categories

#### Petite (155-162 cm)
- **Tops**: Fitted/cropped tops, V-necklines, wrap styles
- **Bottoms**: High-waisted pants/skirts, tapered trousers, skinny jeans
- **Shoes**: Pointed flats, nude heels
- **Accessories**: Small handbags, delicate jewelry, waist belts
- **Colors**: Monochrome outfits, minimal contrasts

#### Average (163-170 cm)
- **Tops**: Peplum tops, tucked-in blouses, cardigans, structured blazers
- **Bottoms**: Straight-leg jeans, midi skirts, tailored pants
- **Shoes**: Ankle boots, flats, wedge sandals
- **Accessories**: Medium-sized handbags, statement earrings, scarves
- **Colors**: Neutral bases with jewel-tone accents

#### Tall (171+ cm)
- **Tops**: Tunics, longline tops, oversized shirts, statement sleeves
- **Bottoms**: Wide-leg pants, palazzos, flared jeans, midi/long skirts
- **Shoes**: Platform sandals, combat boots, bold flats
- **Accessories**: Long pendant necklaces, larger handbags, wide belts
- **Colors**: Bold contrasts, bright palettes, color-blocking

## Testing

### Test the Recommendation System Directly
```bash
python recommendation_system.py
```

This will run tests with both male and female sample measurements and display the recommendations for both genders.

### Test the API
1. Start the server: `python app.py`
2. Use Postman, cURL, or any HTTP client to send POST requests to `http://localhost:5000/recommend`
3. Test with both male and female data to see gender-specific recommendations

## Error Handling

The API returns appropriate HTTP status codes:
- `200`: Success
- `400`: Bad request (missing data, invalid gender, or unsupported gender)
- `500`: Internal server error

Error responses include an `error` field with a description of the issue.

## Future Enhancements

- Integration with real-time fashion trends
- Machine learning-based recommendations
- Image-based body measurement detection
- Seasonal and occasion-based recommendations
- Integration with e-commerce platforms
- Support for additional body measurements and proportions
- Age-based styling recommendations
- Occasion-specific outfit suggestions

## Contributing

Feel free to contribute by:
- Adding new recommendation categories
- Improving the height categorization logic
- Adding support for more body measurements
- Enhancing the API with additional endpoints
- Adding unit tests
- Expanding gender-specific styling advice
- Adding seasonal or trend-based recommendations

## License

This project is open source and available under the MIT License. 