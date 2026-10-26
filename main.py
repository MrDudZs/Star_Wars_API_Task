import requests
import pymongo
from pymongo import MongoClient


try:
    uri = "mongodb://localhost:27017"
    client = MongoClient(uri)
    db = client["starwars"]

    # query test
    # ls = db.characters.find_one({"name": "Luke Skywalker"})
    # print(ls)

    # API test
    # def api_test():
    #     endpoint = "https://swapi.dev/api/starships/9/"
    #     response = requests.get(endpoint)
    #     print(response.status_code)
    # api_test()

    def get_starships_api():
        endpoint = requests.get("https://swapi.dev/api/starships/")
        data = endpoint.json()
        print(data)
    # get_starships_api() # confirm query

    def add_starships_to_db(): # See bug tracking (Importing starships as one object)
        try:
            # Get starships
            endpoint = "https://swapi.dev/api/starships/"
            starships = []
            # Create starships collection
            db = client["starwars"]
            db.create_collection("starships")
            while endpoint: # Loop to get all starships
                response = requests.get(endpoint)
                response.raise_for_status()
                data = response.json()
                starships.extend(data["results"])
                endpoint = data["next"]

                # Add Starships to the collection in db
                # Avoids duplicates
                db.starships.drop()
                result = db.starships.insert_many(starships)
                print(f"Inserted {len(result.inserted_ids)} starships")
            return starships
        except Exception as e:
            print(e)

    # add_starships_to_db()

    def get_people_api():
        endpoint = requests.get("https://swapi.dev/api/people/")
        data = endpoint.json()
        print(data)
    # get_people_api()# confirm query


    def import_new_characters(): # This replaces the get pilots by ID
        # Query ID and Name
        db = client["starwars"]
        # Drop existing characters collection in db:

        try:
            # Get characters from people
            endpoint = "https://swapi.dev/api/people/"
            characters = []
            # Create characters collection
            db = client["starwars"]
            db.create_collection("characters")
            while endpoint: # Loop to get all characters
                response = requests.get(endpoint)
                response.raise_for_status()
                data = response.json()
                characters.extend(data["results"])
                endpoint = data["next"]

                # Add characters to the collection in db
                # Avoids duplicates
                db.characters.drop()
                result = db.characters.insert_many(characters)
                print(f"Inserted {len(result.inserted_ids)} characters")
            return characters
        except Exception as e:
            print(e)



    # import_new_characters()

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


    replace_pilots_and_insert()


except Exception as e:
    raise Exception(
        "The following error occurred: ", e
    )
