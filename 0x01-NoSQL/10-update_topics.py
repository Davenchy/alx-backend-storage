#!/usr/bin/env python3
""" define update_topics function """


def update_topics(mongo_collection, name, topics):
    """ update_topics function """
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
    return mongo_collection
