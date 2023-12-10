import pickle

def dump(obj, file, protocol=pickle.HIGHEST_PROTOCOL):
    with open(file, 'wb') as f:
        pickle.dump(obj, f, protocol=protocol)
    return file

def load(file):
    with open(file, 'rb') as f:
        return pickle.load(f)

def read(file):
    with open(file, 'r') as f:
        return f.read()

def write(file, content):
    with open(file, 'w') as f:
        f.write(content)
    return file
