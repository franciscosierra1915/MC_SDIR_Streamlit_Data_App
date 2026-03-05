from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_USER = os.environ.get("MONGO_USER")
MONGO_PASS = os.environ.get("MONGO_PASS")
MONGO_CLUSTER_URL = os.environ.get("MONGO_CLUSTER_URL")

# print(MONGO_USER, MONGO_PASS, MONGO_CLUSTER_URL)

FINAL_URL = (f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}@{MONGO_CLUSTER_URL}/"
             f"?retryWrites=true&w=majority")
client = MongoClient(FINAL_URL)
# print(client)

db = client['water_quality_data']
robot1 = db["asv_1"]

print(f"Using database: {db} and collection: {robot1}")

obs1 = {"temp": 92,
        "salinity": 35,
        "pH": 6.5,
        "oxygen": 7.2,
        "notes": "good"}

result1 = robot1.insert_one(obs1)

# print("Inserted document id:", result1.inserted_id)

listObs = [
    {"temp": 93, "salinity": 36, "pH": 6.6, "oxygen": 7.3, "notes": "good"},
    {"temp": 94, "salinity": 37, "pH": 6.7, "oxygen": 7.4, "notes": "good"},
    {"temp": 95, "salinity": 38, "pH": 6.8, "oxygen": 7.5, "notes": "good"}
]

result2 = robot1.insert_many(listObs)

# Other methods:

doc = robot1.find_one()

for obs in robot1.find({"temp":{"$gt":28}}): # $gt greater than
    print("Hot water", obs)