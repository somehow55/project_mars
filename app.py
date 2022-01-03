from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:1234@cluster0.8s2if.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.dbhandey


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/mars", methods=["POST"])
def web_mars_post():
    name_receive = request.form['name_receive']
    address_receive = request.form['address_receive']
    size_receive = request.form['size_receive']

    doc = {
        'name':name_receive,
        'address':address_receive,
        'size':size_receive
    }
    db.mars.insert_one(doc);

    return jsonify({'msg': ' 주문 완료!'})

@app.route("/mars", methods=["GET"])
def web_mars_get():
    return jsonify({'msg': 'GET 연결 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)