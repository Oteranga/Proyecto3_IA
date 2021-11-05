import math
from sklearn.neighbors import KDTree
import numpy as np

def distance(centroid,current_row):
    distances = []
    for i in range(len(centroid) - 1):
        distances.append(pow(centroid[i] - current_row[i], 2))
    return [math.sqrt(distance) for distance in distances]

def make_pairs(df):
    df = df.values.tolist()
    pairs = []
    for i in range(len(df)):
        pairs.append((df[i], None))
    return pairs

def range_query(df, point, radius):
    new_df = []
    for set in df:
        new_df.append(set[0])
    new_arrays = np.array(new_df)
    tree = KDTree(new_arrays, leaf_size = 20)
    indices = tree.query_radius(np.array(point).reshape(1, -1), r = radius)
    neighbors = []
    for n in indices:
        neighbors.append((new_arrays[n], df[n][1]))
    return neighbors