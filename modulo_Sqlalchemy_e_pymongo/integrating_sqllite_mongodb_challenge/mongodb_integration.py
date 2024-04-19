import pprint

import pymongo as pyM

# use suas credenciais aqui e seu cluster
client = pyM.MongoClient("mongodb+srv://<nome>:<senha>@<cluster>.8ld7j9w.mongodb.net/?retryWrites=true&w=majority")

db = client.bank
collection = db.test_collection

bank = {
    'name': 'Mike',
    'cpf': '123.123.123-12',
    'address': 'São Paulo',
    'type': 'Conta corrente',
    'agency': '0001',
    'number': 127,
    'balance': '1202.5',
}

accounts = db.accounts
post_id = accounts.insert_one(bank).inserted_id
print(post_id)

print(db.accounts.find_one())

pprint.pprint(db.accounts.find_one())

# bulk insert
new_accounts = [{
    'name': 'Jonas',
    'cpf': '123.123.123-42',
    'address': 'São Francisco',
    'type': 'Conta Poupança',
    'agency': '0001',
    'number': 126,
    'balance': '223.5', },
    {
    'name': 'Julia',
    'cpf': '123.123.123-22',
    'address': 'Rio de Janeiro',
    'type': 'Conta corrente',
    'agency': '0001',
    'number': 129,
    'balance': '402.5', }]

result = accounts.insert_many(new_accounts)
print(result.inserted_ids)

print("\n Recuperando dados do Jonas")
pprint.pprint(db.accounts.find_one({'name': 'Jonas'}))

print("\n Recuperando dados do Mongo")
for post in accounts.find():
    pprint.pprint(post)

# Contando a quantidade de documentos no mongoDB
print(accounts.count_documents({}))
print(accounts.count_documents({'name': 'Mike'}))

print(accounts.find_one({'agency': '0001'}))

print("\n Recuperando de Maneira ordenada")
for post in accounts.find({}).sort("author"):
    pprint.pprint(post)
