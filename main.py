"""
Created by Epic at 9/20/20
"""
from pymongo import MongoClient

mongo_from_uri = input("Mongo (from) URI> ")
mongo_target_uri = input("Mongo (target) URI> ")

database_name = input("Database to copy> ")
table_names = input("Tables to copy (split by ;)> ").split(";")

from_mongo = MongoClient(mongo_from_uri)
target_mongo = MongoClient(mongo_target_uri)

from_database = from_mongo[database_name]
target_database = target_mongo[database_name]

for table in table_names:
    from_table = from_database[table]
    target_table = target_database[table]

    data = list(from_table.find({}))
    if len(data) == 0:
        print(f"Please create table '{table}' manually!")
        continue
    target_table.insert_many(data)
print("Done")
