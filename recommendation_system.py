def categorize_by_measurements(measurements, gender="male"):
    height = measurements.get('subject-height', None)
    categories = []
    if height:
        if gender.lower() == "female":
            if height < 163:
                categories.append('petite')
            elif 163 <= height < 171:
                categories.append('average')
            else:
                categories.append('tall')
        else:  # male
            if height < 167:
                categories.append('short')
            elif 167 <= height < 183:
                categories.append('average')
            else:
                categories.append('tall')
    return categories

def generate_text_recommendation(measurements, gender="male"):
    height = measurements.get('subject-height', None)
    categories = categorize_by_measurements(measurements, gender)
    text = "Analysis Report:\n\n"
    
    if gender.lower() == "female":
        if height:
            if 'petite' in categories:
                text += f"Based on your height ({height} cm), which falls into the petite range (155-162 cm),\nhere are personalized recommendations:\n\n"
            elif 'average' in categories:
                text += f"Based on your height ({height} cm), which falls into the average range (163-170 cm),\nhere are personalized styling suggestions:\n\n"
            else:
                text += f"Based on your height ({height} cm), which places you in the tall category (171+ cm),\nhere are your personalized style recommendations:\n\n"
        else:
            text += "Based on your measurements, here are the personalized recommendations for you:\n\n"
        
        # Female recommendations
        text += "Tops:\n"
        if 'petite' in categories:
            text += "- Fitted or cropped tops help elongate your frame.\n- V-necklines and wrap styles add a vertical illusion.\n- Avoid oversized tops; they can overwhelm your proportions.\n\n"
        elif 'tall' in categories:
            text += "- Tunics, longline tops, and oversized shirts suit your frame well.\n- Use horizontal patterns to balance height.\n- Statement sleeves or crop jackets can add proportion.\n\n"
        else:
            text += "- Peplum tops, tucked-in blouses, and cardigans flatter your height.\n- Structured blazers create an elegant silhouette.\n- Patterns and colors can be mixed confidently.\n\n"
        
        text += "Bottoms:\n"
        if 'petite' in categories:
            text += "- High-waisted pants and skirts elongate the legs.\n- Tapered trousers or skinny jeans maintain a balanced silhouette.\n- Avoid overly wide-leg pants unless they are cropped.\n\n"
        elif 'tall' in categories:
            text += "- Wide-leg pants, palazzos, and flared jeans flatter long legs.\n- Midi or long skirts flow beautifully with your height.\n\n"
        else:
            text += "- Straight-leg jeans, midi skirts, and tailored pants all suit you well.\n- High-rise cuts enhance waist definition.\n\n"
        
        text += "Shoes:\n"
        if 'petite' in categories:
            text += "- Pointed flats or nude heels visually lengthen the legs.\n- Avoid ankle straps that cut the line of your legs.\n\n"
        elif 'tall' in categories:
            text += "- Platform sandals, combat boots, or bold flats look fantastic.\n- Don't shy away from heels—they elevate confidence.\n\n"
        else:
            text += "- Ankle boots, flats, and wedge sandals are stylish and well-proportioned.\n- Minimalist sneakers for casual outings.\n\n"
        
        text += "Accessories:\n"
        if 'petite' in categories:
            text += "- Small handbags and delicate jewelry maintain proportion.\n- Waist belts can create a flattering shape.\n\n"
        elif 'tall' in categories:
            text += "- Long pendant necklaces and larger handbags are balanced on your frame.\n- Wide belts and dramatic scarves can break up long lines.\n\n"
        else:
            text += "- Medium-sized handbags and statement earrings work best.\n- Scarves and belts can add dimension to your outfit.\n\n"
        
        text += "Color Sense:\n"
        if 'petite' in categories:
            text += "- Monochrome outfits add height visually.\n- Stick to minimal contrasts and clean lines.\n\n"
        elif 'tall' in categories:
            text += "- Bold contrasts and bright palettes emphasize your striking presence.\n- Color-blocking works well to segment height.\n\n"
        else:
            text += "- Neutral bases with bright or jewel-tone accents work beautifully.\n- Play with layering and light/dark contrasts.\n\n"
        
        text += "Recommended Color Combinations:\n"
        if 'petite' in categories:
            text += "1. Cream top with beige trousers\n2. Navy blouse with black high-waisted jeans\n3. Blush pink shirt with white pants\n4. Charcoal dress with nude shoes\n5. Light gray top with navy skirt\n"
        elif 'tall' in categories:
            text += "1. Bold red blouse with black wide-leg pants\n2. Beige sweater with navy skirt\n3. Light blue tunic with white trousers\n4. Forest green shirt with tan jeans\n5. Mustard crop jacket with charcoal culottes\n"
        else:
            text += "1. Olive blouse with beige trousers\n2. Teal top with black skirt\n3. White shirt with denim jeans\n4. Lavender sweater with navy pants\n5. Maroon dress with tan shoes\n"
    
    else:  # Male recommendations
        if height:
            if 'short' in categories:
                text += f"Based on your height ({height} cm), which falls into the 160-166 cm range,\nhere are personalized style recommendations:\n\n"
            elif 'average' in categories:
                text += f"Based on your height ({height} cm), which falls into the 175-182 cm range,\nhere are the style suggestions designed for your frame:\n\n"
            else:
                text += f"Based on your height ({height} cm), which places you in the tall category (183+ cm),\nhere are your style guidelines:\n\n"
        else:
            text += "Based on your measurements, here are the personalized recommendations for you:\n\n"
        
        # Male recommendations
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

def generate_search_queries(measurements, gender="male"):
    categories = categorize_by_measurements(measurements, gender)
    
    if gender.lower() == "female":
        if 'petite' in categories:
            top_wear = 'cropped tops for petite women'
            bottom_wear = 'high waist skinny jeans for petite'
            shoes = 'nude heels for petite women'
            color_query = 'monochrome outfits for petite women'
        elif 'tall' in categories:
            top_wear = 'longline tops for tall women'
            bottom_wear = 'wide leg pants for tall women'
            shoes = 'platform sandals for tall women'
            color_query = 'color block fashion for tall women'
        else:
            top_wear = 'peplum tops for women'
            bottom_wear = 'midi skirts for average height women'
            shoes = 'ankle boots for women'
            color_query = 'neutral and jewel tone outfits for women'
    else:  # male
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
        gender = measurements.get('gender', 'male')
        text_recommendation = generate_text_recommendation(measurements, gender)
        search_queries = generate_search_queries(measurements, gender)
        
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
    # Test the system with male measurements
    male_measurements = {
        "subject-height": 170.18,
        "subject-shoulder": 43.18,
        "subject-chest": 86.36,
        "subject-waist": 66.04,
        "subject-hip": 96.52,
        "subject-arm": 54.61,
        "subject-leg": 95.5,
        "gender": "male"
    }
    
    # Test the system with female measurements
    female_measurements = {
        "subject-height": 160.0,
        "subject-shoulder": 38.0,
        "subject-chest": 85.0,
        "subject-waist": 65.0,
        "subject-hip": 90.0,
        "subject-arm": 50.0,
        "subject-leg": 85.0,
        "gender": "female"
    }
    
    print("=== Male Test Result ===")
    male_result = get_recommendations(male_measurements)
    print(male_result)
    
    print("\n=== Female Test Result ===")
    female_result = get_recommendations(female_measurements)
    print(female_result) 