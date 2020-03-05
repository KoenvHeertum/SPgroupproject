from pymongo import MongoClient
from pprint import pprint

client = MongoClient()
db = client.huwebshop
collection = db.profiles
products = collection.find()

# getting the first items name and price
firstitemdict = collection.find_one()  # automatically gives the first item when no argument is given
firstitem = firstitemdict.get('name')
firstitemprice = firstitemdict.get('price').get('selling_price')/100
print('First item in list is: '+firstitem)
print('Price of first item: '+str(firstitemprice))

# getting the average price from all products
tempdoc = collection.distinct('price')
sumprice = 0
for items in tempdoc:
    sumprice += items.get('selling_price')

averageprice = (sumprice / len(tempdoc)) / 100
print('Average price of all items: '+str(averageprice))


# counting how many documents there are with {name}
tempdoc2 = collection.count_documents({'brand':'8x4'})


# how to put something in the database and how to remove an item

# collection.update_one({'_id' : tempdoc.get('_id') }, {'$inc': {'likes': 5}})
# pprint(collection.find_one({'brand':'8x4'}))

# collection.update_one({'_id' : tempdoc.get('_id') }, {'$unset': {'likes': ''}})
# pprint(collection.find_one({'brand':'8x4'}))
