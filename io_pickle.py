import pickle


# The name of the file where we will store the object
shoplistfile = 'shoplist.data'
# The list of things to buy
shoplsit = ['apple', 'mango', 'carrot']

# Write to the file
f = open(shoplistfile, 'wb')
# Dump the object to a file
pickle.dump(shoplsit, f)
f.close()

# Destroy the shoplist variable
del shoplsit

# Read back from the storage
f = open(shoplistfile, 'rb')
# Load the object from the file
storedlist = pickle.load(f)
print(storedlist)
f.close()