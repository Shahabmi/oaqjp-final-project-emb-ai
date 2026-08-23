from flask import Flask,request,render_template
from EmotionDetection.emotion_detection import emotion_detector

app=Flask(__name__)

@app.route('/')
def starter():
    return render_template('index.html')


@app.route('/emotionDetector')
def emotion_detector_func():
    text_to_analyze=request.args.get('textToAnalyze')
    result=emotion_detector(text_to_analyze)
    res= (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, " 
        f"'fear': {result['fear']}, " 
        f"'joy': {result['joy']} and " 
        f"'sadness': {result['sadness']}. " 
        f"The dominant emotion is <strong>{result['dominant_emotion']}</strong>.")
    return res



if __name__=='__main__':
    app.run(port=5000)

