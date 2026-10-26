from pymongo import MongoClient
import requests

uri = "mongodb://localhost:27017"
client = MongoClient(uri)
db = client["starwars"]


def get_starships_api():
    endpoint = requests.get("https://swapi.dev/api/starships/")
    data = endpoint.json()
    print(data)


# get_starships_api() # confirm query
def add_starships_to_db():

    # See bug tracking (Importing starships as one object)
    try:
        # Get starships
        endpoint = "https://swapi.dev/api/starships/"
        starships = []
        # Create starships collection
        db = client["starwars"]
        db.create_collection("starships")
        while endpoint:  # Loop to get all starships
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