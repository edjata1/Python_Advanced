# object serialization = process of converting "state of an object" into "byte stream"
# "byte stream" = can be stored in any "file-like" object such as "disk file" or "memory stream"
# serialization (dump() & dumps()) and deserialization (load() & loads())by pickling and unpickling

# import pickle package
import pickle

# open file pickled.txt and write in binary model
f=open("pickled.txt", "wb")

# create dictionary - dictionary are unordered
dct={"name":"Empress", "age": 27, "Gender":"Female", "marks": 95}

# dump dct into file pickled.txt
pickle.dump(dct, f)

# close file
f.close()

from pickle import dumps
dctstring = dumps(dct)

print(dctstring)

from pickle import loads
dct = loads(dctstring)
print(dct)

# import pickle

def storeData():
    # initializing data to be stored in db
    Tim = {'key':'Tim', 'name': 'Tim White', 'age': 22, 'pay': 69000}
    Jon = {'key':'Jon', 'name': 'Jon White', 'age': 49, 'pay': 49000}

    # database
    db = {}
    db['Tim'] = Tim
    db['Jon'] = Jon

    # It's important to use binary mode
    dbfile = open('examplePickle', 'ab')

    # source,destination
    pickle.dump(db, dbfile)
    dbfile.close()

def loadData():
    # for reading also binary mode is important
    dbfile = open('examplePickle', 'rb')

    db = pickle.load(dbfile)

    for keys in db:
        print(keys, '=>', db[keys])

    dbfile.close()
