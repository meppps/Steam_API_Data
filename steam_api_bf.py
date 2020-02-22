# Module used to connect Python with MongoDb
import pymongo

# The default port used by MongoDB is 27017
# https://docs.mongodb.com/manual/reference/default-mongodb-port/
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define the database in Mongo
db = client.steamDB

# Check if database exists
print(client.list_database_names()) # prints all database names

db_list = client.list_database_names() # prints specific database name
if YOUR_DB_HERE in db_list:
    print("The database exists.")

# Check if collection exists
print(db.list_collection_names()) # prints all collections 

col_list = db.list_collection_names() # prints specific collection 
if YOUR_COLLECTION_HERE in col_list:
    print("Collection exists.")


