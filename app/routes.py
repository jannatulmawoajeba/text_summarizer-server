from flask import Flask, request, jsonify
from flask_cors import CORS
from app import app
from app.summarizer import Summarizer, nlp



@app.route('/', methods=['GET'])
def index():
    return ('Hello from Server!')


@app.route('/summarize', methods=['POST'])
def summarize():
    summarizer = Summarizer(nlp)
    data = request.get_json()
    input_text = data.get('input_text', '')
    num_sentences = 5
    summary = summarizer.summarize_text(input_text, num_sentences)
    return jsonify({'result': summary})

