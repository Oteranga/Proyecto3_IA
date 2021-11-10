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
    def __init__(self, sample, tissue):
        self.cluster = -1
        self.data = sample
        self.type = tissue

    def set_cluster(self, new_cluster):
        self.cluster = new_cluster
    
    def print_pair(self):
        print("{",self.cluster,",",self.type,"}")
    
    def __eq__(self, other):
        comparison = self.data == other.data
        equal_arrays = comparison.all()
        return equal_arrays