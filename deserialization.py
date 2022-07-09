# deserialize/unpickle/load
import pickle

# opening file in read and binary mode  - dictionary are unordered
f=open("pickled.txt", "rb")

# load into d to deserialize what's in pickled.txt
d=pickle.load(f)

# print
print(d)

# close stream
f.close()

