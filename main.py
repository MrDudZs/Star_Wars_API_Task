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
            while endpoint: # Loop
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


    def get_pilot_ids():
        # Query ID and Name

        db = client["starwars"]

        print(db.characters.find_one(
            {},
            {"_id": 1, "name": 1}
        ))

        # Goal to filter by ship type
        # Find ship type in person data and then add that persons id value as pilot to ships data
        # plan: re-import with newest dataset (using old characters' dataset)
        # filter by characters with starships, and display starship, _id, name

    # get_pilot_ids()

    def replace_pilots_and_insert():
        set
        # Goal once get_pilot_ids is done
        # use the query of get_pilots_id, then check starships in persons field and match to name in starship field.
        # add persons _id to the pilots column in star ships

except Exception as e:
    raise Exception(
        "The following error occurred: ", e
    )
