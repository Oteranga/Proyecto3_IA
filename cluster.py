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