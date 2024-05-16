#!/usr/bin/env python3
"""
Stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')

    database_name = 'logs'
    collection_name = 'nginx'
    # Access the specified collection
    collection = client[database_name][collection_name]

    # Total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Methods stats
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({'method': method})
        print(f"\tmethod {method}: {count}")

    # Stats for method=GET and path=/status
    status_count = collection.count_documents(
                   {'method': 'GET', 'path': '/status'}
                   )
    print(f"{status_count} status check")