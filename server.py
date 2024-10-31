"""
This module provides a Flask web server to analyze emotions from user-provided text.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """Renders the home page."""
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_route():
    """Detects emotions from the provided text."""
    text_to_analyze = request.args.get('textToAnalyze')
    if text_to_analyze == '':
        return "<h2>Invalid text! Please try again!<h2>"
    # calling emotion detector function
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    output=(f"For the given statement, the system response is 'anger': {response['anger_score']}, "
              f"'disgust': {response['disgust_score']}, 'fear': {response['fear_score']}, "
              f"'joy': {response['joy_score']} and 'sadness': {response['sadness_score']}. "
              f"The dominant emotion is {response['dominant_emotion']}.")
    return output

if __name__ == "__main__":
    app.run(debug=True, port=5000)
