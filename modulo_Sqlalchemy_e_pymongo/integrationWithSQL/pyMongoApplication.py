import pprint

import pymongo as pyM

# use suas credenciais aqui e seu cluster
client = pyM.MongoClient("mongodb+srv://<nome>:<senha>@<cluster>.8ld7j9w.mongodb.net/?retryWrites=true&w=majority")

db = client.test
collection = db.test_collection

post = {
    'author': 'Mike',
    'text': 'First mongodb application with python',
    'tags': ["mongodb", "python3", "pymongo"],
}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

print(db.posts.find_one())

pprint.pprint(db.posts.find_one())

#bulk insert
new_posts = [{
    'author': 'Mike',
    'text': 'another post',
    'tags': ["bulk", "post", "insert"],},
    {
    'author': 'Joao',
    'text': 'Second mongodb application with python',
    'tile': 'Mongo is fun'}]

result = posts.insert_many(new_posts)
print(result.inserted_ids)

print("\n Recuperando dados do Joao")
pprint.pprint(db.posts.find_one({'author':'Joao'}))

print("\n Recuperando dados do Mongo")
for post in posts.find():
    pprint.pprint(post)
