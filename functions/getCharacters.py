from pymongo import MongoClient
import requests

uri = "mongodb://localhost:27017"
client = MongoClient(uri)
db = client["starwars"]

def get_people_api():
    endpoint = requests.get("https://swapi.dev/api/people/")
    data = endpoint.json()
    print(data)


# get_people_api() # confirm query

def import_new_characters():
    # This replaces the get pilots by ID
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
        while endpoint:  # Loop to get all characters
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