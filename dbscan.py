import aux as a

def dbscan(df, r, min_points):
    df = a.makePairs(df)
    cluster = 0
    list_clusters = []
    for point in df:
        if point[1] != None: #With label
            continue
        neighbors = a.rangeQuery(df, point[0], r)
        if len(neighbors) < min_points: #Atypical values
            point[1] = False
            continue
        cluster += 1
        point[1] = cluster
        neighbors.remove(point)
        new_cluster = neighbors
        for val in neighbors:
            if val[1] == False:
                val[1] = cluster
            elif val[1] != None:
                continue
            new_neighbors = a.rangeQuery(df, val[0], r)
            val[1] = cluster
            if len(new_neighbors) < min_points:
                continue
            new_cluster += new_cluster + new_neighbors
        list_clusters.append(new_cluster)
            
