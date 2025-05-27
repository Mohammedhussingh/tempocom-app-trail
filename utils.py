import pandas as pd

def get_mart(path):
    if 'private' in path:
        #return pd.read_csv(path, token=token)
        return pd.read_csv(path)
    else:
        return pd.read_csv(path)