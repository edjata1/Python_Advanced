import pickle

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

