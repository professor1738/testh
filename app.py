# app.py

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

WAYBACK_API_URL = "https://web.archive.org/cdx/search/cdx"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    target_url = request.form.get('target_url')

    params = {'url': target_url, 'output': 'json'}
    response = requests.get(WAYBACK_API_URL, params=params)

    wayback_urls = [entry[2] for entry in response.json()] if response.ok else []

    return render_template('result.html', wayback_urls=wayback_urls)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
