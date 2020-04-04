from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

Avengers = db.movies.find_one({'title' : '어벤져스: 엔드게임'})
Ranking = db.movies.update_many({'star' : Avengers['star']}, {'$set' : {'star' : '0'}})
