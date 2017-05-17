import os
import json
import sys
from flask import Flask, jsonify, request
from watson_developer_cloud import ToneAnalyzerV3, VisualRecognitionV3, LanguageTranslatorV2

app = Flask(__name__)
vcap = os.getenv("VCAP_SERVICES")
vcap = json.loads(vcap)

@app.route("/")
def home():
    return "Hello World!"

@app.route("/version")
def version():
    return sys.version

@app.route("/translate", methods=['POST'])
def translate():
    password = vcap['language_translator'][0]['credentials']['password']
    url = vcap['language_translator'][0]['credentials']['url']
    username = vcap['language_translator'][0]['credentials']['username']
    language_translator = LanguageTranslatorV2(username=username, password=password)
    output = language_translator.translate(text=request.json['text'], source='en', target='es')
    return jsonify({'output': output})

@app.route("/visual", methods=['POST'])
def visual():
    api_key = vcap['watson_vision_combined'][0]['credentials']['api_key']
    note = vcap['watson_vision_combined'][0]['credentials']['note']
    url = vcap['watson_vision_combined'][0]['credentials']['url']
    visual_recognition = VisualRecognitionV3(api_key=api_key, version='2016-05-20')
    output = visual_recognition.classify(images_url=request.json['url'])
    return jsonify(output)

@app.route("/tone", methods=['POST'])
def tone():
    password = vcap['tone_analyzer'][0]['credentials']['password']
    url = vcap['tone_analyzer'][0]['credentials']['url']
    username = vcap['tone_analyzer'][0]['credentials']['username']
    tone_analyzer = ToneAnalyzerV3(username=username, password=password, version='2016-05-19')
    output = tone_analyzer.tone(request.json['text'])
    return jsonify(output)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 9099))
    app.run(host='0.0.0.0', port=port)

# from IPython import embed
# embed()
