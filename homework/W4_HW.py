from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('W1_Thur_HW_수정.html')


@app.route('/purchaseinfo', methods=['POST'])
def write_info():
    name_receive = request.form['name_give']
    quantity_receive = request.form['quantity_give']
    address_receive = request.form['address_give']
    phonenumber_receive = request.form['phonenumber_give']
    price_receive = request.form ['price_give']

    purchaseinfo = {'name': name_receive, 'quantity': quantity_receive, 'address': address_receive,
                    'phonenumber': phonenumber_receive, 'price': price_receive}

    db.purchaseinfo.insert_one(purchaseinfo)

    return jsonify({'result': 'success', 'msg': '저장완료!'})


@app.route('/purchaseinfo')
def find_info():
    buyers = list(db.purchaseinfo.find({}, {'_id':0}))
    return jsonify({'result': 'success', 'buyers_info': buyers})





if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)