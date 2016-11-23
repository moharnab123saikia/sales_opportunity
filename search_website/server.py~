from flask import Flask
import findValues
from flask import request
import json
from flask import render_template, send_from_directory

app = Flask(__name__)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('./static/js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('./static/css', path)


@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('./static/img', path)


@app.route('/')
def ind():
    return render_template('./index.html')
    
@app.route('/search', methods=['GET'])
def search():
    if request.method == 'GET':
    	print request.args.get('price')
        price = request.args.get('price')
        features_in = request.args.get('features')
        features = features_in.split(',')

        k = findValues.get_top_values(int(price), features[:5])
        k1 = findValues.get_random_values(int(price), features[5:])
        k.update(k1)
        return str(k)
    return "{}"
