from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://mongo:{password}@cluster0.hgeu2q2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


client = MongoClient(connection_string)

dbs = client.list_database_names()


production = client.production
person_collection = production.person_collection

def create_documents():
    first_names = ["Tim", "Sarah", "Jennifer", "Jose", "Brad", "allen"]
    last_names = ["Rusica", "Smith", "Bart", "Carter", "Pit", "Geral"]
    ages = [21, 40, 23, 19, 34, 67]

    docs = []

    for first_name, last_name, age in zip(first_names, last_names, ages):
        doc = {"first_name": first_name, "last_name": last_name, "age": age}
        docs.append(doc)
       
       # person_collection.insert_one(doc)
    person_collection.insert_many(docs)

create_documents()