# -*- coding: utf-8 -*-
"""Copy of DS6_Lambda_MongoDB_Playground.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RB14drzyJg7u4f-wH27lc3xjB42wHu7U

# MongoDB with PyMongo

LSDS Unit 3 Sprint 2 Module 3

Some resources:

https://docs.atlas.mongodb.com/getting-started/

https://api.mongodb.com/python/current/

HN Discussion on MongoDB versus PostgreSQL/SQLite: https://news.ycombinator.com/item?id=19158854
"""

#Pull out the IP address for this colab notebook
!curl ipecho.net/plain

"""user: admin  
pass: U3RLFYpO1NrdcIFv
"""

# How do we figure out our python version?
import sys
print(sys.version)

!pip install pymongo

import pymongo

# Use 3.4 connection string for clarity
client = pymongo.MongoClient("mongodb://admin:U3RLFYpO1NrdcIFv@cluster0-shard-00-00-wk9ed.mongodb.net:27017,cluster0-shard-00-01-wk9ed.mongodb.net:27017,cluster0-shard-00-02-wk9ed.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

db

# check how many machines
client.nodes

help(db)

db.test

dir(db.test)

help(db.test.insert_one)

#Count how many documents
db.test.count_documents({'x':1})

db.test.insert_one({'x': 1})

#Count again
db.test.count_documents({'x':1})

db.test.insert_one({'x': 1})

db.test.count_documents({'x': 1})

db.test.find_one({'x': 1})

curs = db.test.find({'x': 1})

dir(curs)

list(curs)

jason_doc = {
    'favorite animal': ['Shark', 'Cats']
}

matthew_doc = {
    'favorite animal': 'Platypus'
}

nick_doc = {
    'favorite animal': 'Hippogriff'
}

db.test.insert_many([jason_doc, matthew_doc, nick_doc])

list(db.test.find())

# Now let's make more docs

more_docs = []
for i in range(10):
  doc = {'even': i % 2 == 0}
  doc['value'] = i
  more_docs.append(doc)

more_docs

db.test.insert_many(more_docs)

list(db.test.find({'even':False}))

list(db.test.find({'favorite animal': 'Platypus'}))

"""CRUD - Create Read Update Delete"""

help(db.test.update_one)

help(db.test.delete_one)

db.test.update_one({'value': 3},
                  {'$inc': {'value': 5}})

list(db.test.find())

db.test.update_many({'even': True},
                    {'$inc': {'value': 100}})

list(db.test.find({'even': True}))

db.test.delete_many({'even': False})

list(db.test.find())

rpg_character = (1, "King Bob", 10, 3, 0, 0, 0)

#This gets error because rpg_character is not a dict
# db.test.insert_one(rpg_character)

#Wrap it in a simple dictionary so that the insert_one method works
db.test.insert_one({'rpg_character': rpg_character})

db.test.insert_one({
    'sql_id': rpg_character[0],
    'name': rpg_character[1],
    'hp': rpg_character[2],
    'level': rpg_character[3]
})

list(db.test.find())