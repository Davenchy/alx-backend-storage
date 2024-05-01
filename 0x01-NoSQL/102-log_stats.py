#!/usr/bin/env python3
""" This script logs statistics about Nginx logs stored in MongoDB """
from pymongo import MongoClient
from pprint import pprint


METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
if __name__ == "__main__":

    with MongoClient() as client:
        docs = client.logs.nginx

        def countMethod(methodName):
            return {
                '$sum': {
                    '$cond': [{'$eq': ['$method', methodName]}, 1, 0]
                }
            }

        results = docs.aggregate([
            {
                '$group': {
                    '_id': None,
                    'count': {'$sum': 1},
                    'status': {
                        '$sum': {
                            '$cond': [{'$and': [
                                {'$eq': ['$method', 'GET']},
                                {'$eq': ['$path', '/status']}
                            ], }, 1, 0]
                        }
                    },
                    **{
                        method: countMethod(method)
                        for method in METHODS
                    }
                }
            }
        ]).next()

        log = "{logs} logs\nMethods:\n{methods}\n{status} status check\nIPs:"
        print(log.format(
            logs=results["count"],
            methods="\n".join(
                f"\tmethod {method}: {results.get(method, 0)}"
                for method in METHODS
            ),
            status=results["status"]
        ))

        ips = docs.aggregate([
            {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 10}
        ])

        for ip in ips:
            print(f"\t{ip['_id']}: {ip['count']}")
