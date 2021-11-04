import aux as a

def dbscan(df, r, minPoints):
    df = a.makePairs(df)
    cluster = 0
    for point in df:
        if point[1] == None: #Without label
            neighbors = a.rangeQuery(df, point[0], r)
            if len(neighbors) < minPoints: #Atypical values
                point[1] = False
                continue
            cluster += 1
            point[1] = cluster
            
