import requests
import pymongo
from pymongo import MongoClient
from functions.getStarships import add_starships_to_db
from functions.getCharacters import import_new_characters
from functions.givePilotID import replace_pilots_and_insert

try:

    add_starships_to_db()
    import_new_characters()
    replace_pilots_and_insert()
except Exception as e:
    raise Exception(
        "The following error occurred: ", e
    )


