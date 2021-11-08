import collections

class Cluster:
    def __init__(self,centroid):
        self.centroid = centroid
        self.samples = []
    
    def add_sample(self,sample):
        self.samples.append(sample)
    
    def print_samples(self):
        size = len(self.samples[0])
        for sample in self.samples:
            print(sample[size-1])
    
    def get_frequency(self):
        size = len(self.samples[0])
        tissues = []
        for sample in self.samples:
            tissues.append(sample[size-1])
        counter = collections.Counter(tissues)
        return counter

class Pair:
    def __init__(self, sample):
        self.cluster = 0
        self.data = sample

    def setCluster(self, newCluster):
        self.cluster = newCluster