def categorize_by_measurements(measurements):
    height = measurements.get('subject-height', None)
    categories = []
    if height:
        if height < 167:
            categories.append('short')
        elif 167 <= height < 183:
            categories.append('average')
        else:
            categories.append('tall')
    return categories

def generate_text_recommendation(measurements):
    height = measurements.get('subject-height', None)
    categories = categorize_by_measurements(measurements)
    text = "Analysis Report:\n\n"
    if height:
        if 'short' in categories:
            text += f"Based on your height ({height} cm), which falls into the 160-166 cm range,\nhere are personalized style recommendations:\n\n"
        elif 'average' in categories:
            text += f"Based on your height ({height} cm), which falls into the 175-182 cm range,\nhere are the style suggestions designed for your frame:\n\n"
        else:
            text += f"Based on your height ({height} cm), which places you in the tall category (183+ cm),\nhere are your style guidelines:\n\n"
    else:
        text += "Based on your measurements, here are the personalized recommendations for you:\n\n"
    
    # Differentiated general recommendations
    text += "Tops:\n"
    if 'short' in categories:
        text += "- Vertical stripes or monochrome outfits will elongate your frame visually.\n- Shorter-length jackets and shirts that hit just above the hip are ideal.\n- Avoid oversized layers; opt for structured fits.\n\n"
    elif 'tall' in categories:
        text += "- Longline or oversized shirts and jackets work very well.\n- Try layering with hoodies, shackets, and coats.\n- Avoid clothes that are too short—they can exaggerate height awkwardly.\n\n"
    else:
        text += "- Button-up shirts and Henleys work great for your height.\n- Experiment with layering: jackets, overshirts, or cardigans.\n- Try bold or oversized prints occasionally—they won't overwhelm your frame.\n\n"
    
    text += "Bottoms:\n"
    if 'short' in categories:
        text += "- Slim or skinny jeans/pants will provide a sleeker look.\n- Cropped or ankle-length trousers can enhance height perception.\n\n"
    elif 'tall' in categories:
        text += "- Relaxed-fit trousers or straight jeans look best on taller frames.\n- Opt for high-waisted pants to balance torso length.\n\n"
    else:
        text += "- Chinos, slim jeans, and cargo pants all work well.\n- Rolled cuffs or cropped styles help break vertical monotony.\n\n"
    
    text += "Shoes:\n"
    if 'short' in categories:
        text += "- Chelsea boots or slight heel shoes give a refined lift.\n- Avoid bulky footwear that may disrupt body proportion.\n\n"
    elif 'tall' in categories:
        text += "- Chunky sneakers or boots match the proportions of a taller figure.\n- Avoid extremely narrow shoe silhouettes.\n\n"
    else:
        text += "- Brogues, sneakers, or lace-ups all work without overpowering your look.\n- High-tops can be a stylish choice for streetwear outfits.\n\n"
    
    text += "Accessories:\n"
    if 'short' in categories:
        text += "- Narrow belts will avoid cutting the body line horizontally.\n- Choose minimal backpacks or crossbody bags.\n\n"
    elif 'tall' in categories:
        text += "- Tall backpacks or messenger bags suit your length.\n- Wide leather bands or statement watches work well.\n\n"
    else:
        text += "- Long scarves, satchels, or messenger bags can be used stylishly.\n- Leather straps or layered bracelets add elegance.\n\n"
    
    text += "Color Sense:\n"
    if 'short' in categories:
        text += "- Monochrome dressing in darker shades enhances vertical lines.\n- Avoid high-contrast top and bottom pairing.\n\n"
    elif 'tall' in categories:
        text += "- Play with contrasts to break verticality.\n- Use layered neutrals and bold accents.\n\n"
    else:
        text += "- Mix bold and muted tones based on the occasion.\n- Layer colors with a neutral base for depth.\n\n"
    
    text += "Recommended Color Combinations:\n"
    if 'short' in categories:
        text += "1. Charcoal shirt with dark gray jeans\n2. Navy T-shirt with black pants\n3. Olive shirt with charcoal chinos\n4. All-black outfit with brown shoes\n5. Beige T-shirt with khaki pants\n"
    elif 'tall' in categories:
        text += "1. Forest green shirt with cream trousers\n2. Light denim jacket with black jeans\n3. Camel coat with charcoal pants\n4. Burgundy T-shirt with navy jeans\n5. White hoodie with olive joggers\n"
    else:
        text += "1. Maroon shirt with khaki chinos\n2. Mustard yellow hoodie with dark jeans\n3. Gray sweater with black trousers\n4. White Henley with navy chinos\n5. Teal shirt with beige pants\n"
    
    return text

def generate_search_queries(measurements):
    categories = categorize_by_measurements(measurements)
    if 'short' in categories:
        top_wear = 'vertical striped shirts for men'
        bottom_wear = 'cropped pants for short men'
        shoes = 'chelsea boots for men'
        color_query = 'monochrome outfits for short men'
    elif 'tall' in categories:
        top_wear = 'longline jackets for tall men'
        bottom_wear = 'high waist pants for tall men'
        shoes = 'chunky sneakers for men'
        color_query = 'contrast layering for tall men'
    else:
        top_wear = 'henley shirts for men'
        bottom_wear = 'chinos for tall men'
        shoes = 'lace up brogues for men'
        color_query = 'smart casual color combinations for men'
    
    return {
        "top_wear_search_engine_query": top_wear,
        "bottom_wear_search_engine_query": bottom_wear,
        "shoes_search_engine_query": shoes,
        "color_recommendations_search_engine_query": color_query
    }

def get_recommendations(measurements):
    """
    Main function that processes measurements and returns complete recommendations
    """
    try:
        text_recommendation = generate_text_recommendation(measurements)
        search_queries = generate_search_queries(measurements)
        
        response_data = {
            "text_recommendations": text_recommendation,
            **search_queries
        }
        
        return {
            "status": "success",
            "data": response_data
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }

if __name__ == "__main__":
    # Test the system
    measurements = {
        "subject-height": 170.18,
        "subject-shoulder": 43.18,
        "subject-chest": 86.36,
        "subject-waist": 66.04,
        "subject-hip": 96.52,
        "subject-arm": 54.61,
        "subject-leg": 95.5
    }
    
    result = get_recommendations(measurements)
    print("Test Result:")
    print(result) 