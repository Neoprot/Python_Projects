import pprint
import pymongo as pyM

client = pyM.MongoClient("mongodb+srv://kauaseichi:jBOaferNhNLcglJa@cluster0.8ld7j9w.mongodb.net/?retryWrites=true&w=majority")

db = client.test
posts = db.posts

for post in posts.find():
    pprint.pprint(post)

print(posts.count_documents({}))
print(posts.count_documents({'author': 'Mike'}))

print(posts.find_one({'tags': 'insert'}))

print("\n Recuperando de Maneira ordenada")
for post in posts.find({}).sort("author"):
    pprint.pprint(post)

print("\n Espaço")
results = db.profiles.create_index([("author", pyM.ASCENDING)], unique=True)
print(sorted(list(db.profiles.index_information())))

user_profile_user = [
    {'user_id': 211, 'name': 'Luke'},
    {'user_id': 212, 'name': 'Jonas'}]

result = db.profiles_user.insert_many(user_profile_user)

collections = db.list_collection_names()
for collection in collections:
    pprint.pprint(collection)

for post in posts.find():
    pprint.pprint(post)

