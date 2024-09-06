import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)

    regularResponse = json.loads(response.text)

    beforeDictionary = {
        'anger': regularResponse['emotionPredictions'][0]['emotion']['anger'],
        'disgust': regularResponse['emotionPredictions'][0]['emotion']['disgust'],
        'fear': regularResponse['emotionPredictions'][0]['emotion']['fear'],
        'joy': regularResponse['emotionPredictions'][0]['emotion']['joy'],
        'sadness': regularResponse['emotionPredictions'][0]['emotion']['sadness'],
    }
    most = 0
    k = ''
    for key in beforeDictionary:
        if beforeDictionary[key] > most:
            most = beforeDictionary[key]
            k = key

    dictionary = {
        'anger': regularResponse['emotionPredictions'][0]['emotion']['anger'],
        'disgust': regularResponse['emotionPredictions'][0]['emotion']['disgust'],
        'fear': regularResponse['emotionPredictions'][0]['emotion']['fear'],
        'joy': regularResponse['emotionPredictions'][0]['emotion']['joy'],
        'sadness': regularResponse['emotionPredictions'][0]['emotion']['sadness'],
        'dominant_emotion': k,
    }
    return dictionary