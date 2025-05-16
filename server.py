"""Flask web server for Watson NLP emotion detection."""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """Render the homepage with the input form."""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    """
    Handle GET request for emotion detection.
    Extracts the user input from query parameters, processes it using
    the Watson NLP emotion detector, and returns a formatted string response.
    Handles blank inputs by returning an appropriate error message.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Message: Invalid text! Please try again!"

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    return (f"For the given statement, the system response is "
              f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
              f"'joy': {joy} and 'sadness': {sadness}. "
              f"The dominant emotion is {dominant_emotion}.")

if __name__ == '__main__':
    app.run(debug=True)
