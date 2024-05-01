#!/usr/bin/env python3
""" This script logs statistics about Nginx logs stored in MongoDB """
from pymongo import MongoClient
from pprint import pprint


METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
if __name__ == "__main__":

    with MongoClient() as client:
        docs = client.logs.nginx

        print(f'{docs.count_documents({})} logs')
        print('Methods:')

        for method in METHODS:
            count = docs.count_documents({"method": method})
            print(f'\tmethod {method}: {count}')

        statusCount = docs.count_documents({
            "method": "GET", "path": "/status"
        })
        print(f'{statusCount} status check')

        print('IPs:')

        ips = docs.aggregate([
            {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 10}
        ])
        for ip in ips:
            print(f"\t{ip['_id']}: {ip['count']}")
