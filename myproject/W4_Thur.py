from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta


## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/reviews', methods=['POST'])
def write_reviews():
    title_receive = request.form['title_give']
    author_receive = request.form['author_give']
    review_receive = request.form['review_give']

    review = {'title':title_receive, 'author': author_receive, 'review':review_receive}

    db.reviews.insert_one(review)

    return jsonify({'result': 'success', 'msg': '리뷰가 성공적으로 작성되었습니다.'})


@app.route('/reviews')
def find_reviews():

    reviews = list(db.reviews.find({}, {'_id':0}))
    return jsonify({'result' : 'success', 'msg' : '리뷰를 조회하였습니다.', 'reviews': reviews})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)