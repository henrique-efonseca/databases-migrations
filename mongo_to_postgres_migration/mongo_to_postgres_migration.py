import yaml
import pymongo
import psycopg2
from psycopg2 import sql

def get_config():
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config

def migrate_collection(mongo_collection, pg_conn, collection_name):
    pg_cursor = pg_conn.cursor()
    mongo_docs = mongo_collection.find()

    for doc in mongo_docs:
        columns = []
        values = []
        placeholders = []

        for key, value in doc.items():
            if key == '_id':
                key = 'id'
            columns.append(key)
            values.append(value)
            placeholders.append('%s')

        insert_query = sql.SQL("INSERT INTO {} ({}) VALUES ({})").format(
            sql.Identifier(collection_name),
            sql.SQL(', ').join(map(sql.Identifier, columns)),
            sql.SQL(', ').join(sql.Placeholder() * len(placeholders))
        )

        try:
            pg_cursor.execute(insert_query, values)
        except Exception as e:
            print(f"Error inserting document {doc['_id']}: {e}")

    pg_conn.commit()
    pg_cursor.close()

def main():
    config = get_config()

    # MongoDB connection
    mongo_client = pymongo.MongoClient(config['mongodb']['uri'])
    mongo_db = mongo_client[config['mongodb']['database']]

    # PostgreSQL connection
    pg_conn = psycopg2.connect(
        dbname=config['postgresql']['dbname'],
        user=config['postgresql']['user'],
        password=config['postgresql']['password'],
        host=config['postgresql']['host'],
        port=config['postgresql']['port']
    )

    for collection in config['collections']:
        mongo_collection = mongo_db[collection['name']]
        migrate_collection(mongo_collection, pg_conn, collection['name'].lower())

    pg_conn.close()
    mongo_client.close()
    print("Data migration completed.")

if __name__ == "__main__":
    main()
