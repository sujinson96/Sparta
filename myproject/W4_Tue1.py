from pymongo import MongoClient
client = MongoClient ('localhost', 27017)
db = client.dbsparta

all_users = list(db.users.find())
same_age = list(db.users.find({'age' : '20'}))

person = db.users.find_one({'name' : '재혁'})

print(person)