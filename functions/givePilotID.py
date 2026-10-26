from pymongo import MongoClient
import requests

uri = "mongodb://localhost:27017"
client = MongoClient(uri)
db = client["starwars"]

def replace_pilots_and_insert():
    db = client["starwars"]

    # Clear existing pilots
    db.starships.update_many({}, {"$set": {"pilots": []}})

    # Find characters that have starships
    for char in db.characters.find({"starships": {"$ne": []}}, {"_id": 1, "starships": 1}):
        for ship_url in char["starships"]:
            # Match starship by its url field, add character _id to pilots
            db.starships.update_one(
                {"url": ship_url},
                {"$addToSet": {"pilots": char["_id"]}}
            )