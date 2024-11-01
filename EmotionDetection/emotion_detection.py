import requests

def emotion_detector(text_to_predict):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'
    }
    data = {
        "raw_document": {
            "text": text_to_predict
        }
    }
    response = requests.post(url, headers=headers, json=data)
    
    # Handling for response codes
    if response.status_code == 400:
        keys = [
            'anger',
            'disgust',
            'fear',
            'joy',
            'sadness',
            'dominant emotion'
        ]
        return {key: None for key in keys}
    
    emotions = response.json()['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)
    emotions["dominant_emotion"] = dominant_emotion
    
    return emotions