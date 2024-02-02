from pymongo import MongoClient
	
MONGO_URI = 'mongodb://192.168.145.90:27017/'

client = MongoClient(MONGO_URI)
db = client ['rkfassets']
collection = db['devices']

#ollection.insert_one({"hostName": "Switch_VSS", "hostIP": "192.168.130.10"})

switch_one = {"hostName": "SWA-WELLS", "hostIP": "192.168.130.195"}
switch_two = {"hostName": "SWA-WHOUSE", "hostIP": "192.168.130.181"}
collection.insert_many([switch_one, switch_two])

results= collection.find()
for r in results:
    print(r['hostName'])