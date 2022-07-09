import pickle

def loadData():
    # for reading also binary mode is important
    dbfile = open('examplePickle', 'rb')

    db = pickle.load(dbfile)

    for keys in db:
        print(keys, '=>', db[keys])

    dbfile.close()