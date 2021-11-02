import math

def distance(centroid,current_row):
    dist = 0
    for i in range(len(centroid)):
        dist += pow(centroid[i] - current_row[i], 2)
    return math.sqrt(dist)

def makePairs(df):
    df = df.values.tolist()
    pairs = []
    for i in range(len(df)):
        pairs.append((df[i], False))
    return pairs