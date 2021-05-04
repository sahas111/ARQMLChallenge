"""
This script is to build a RESTful Flask service to serve model inferences against arbitrary user-supplied text.
It returns
– a json key with an associated value noting the prediction (POSITIVE/NEGATIVE); and
– a json key with an associated value noting the confidence score, in the range 0-100 and rounded to the nearest integer value.
"""

from flask import abort, Flask, jsonify, request
from transformers import pipeline
import torch
model = pipeline("sentiment-analysis")
import math

app = Flask(__name__)

# @app.route('/api/v1/analyzeSentiment', methods=['POST'])
@app.route('/', methods=['POST'])
def analyzeSentiment():
    if not request.json or not 'message' in request.json:
        abort(400)
    message = request.json['message']
    prediction = model(message)[0]
    response = {'result': prediction['label'], 'confidence_score': math.ceil(prediction['score']*100)}
    return jsonify(response), 200

if __name__ == "__main__":
    app.run()