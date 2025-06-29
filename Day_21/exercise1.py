class Statistics:
    def __init__(self, data):
        self.data = sorted(data)
    
    def count(self):
        return len(self.data)
    
    def sum(self):
        return sum(self.data)
    
    def min(self):
        return min(self.data)
    
    def max(self):
        return max(self.data)
    
    def range(self):
        return self.max() - self.min()
    
    def mean(self):
        return round(self.sum() / self.count())
    
    def median(self):
        n = self.count()
        mid = n // 2
        if n % 2 == 0:
            return (self.data[mid - 1] + self.data[mid]) / 2
        else:
            return self.data[mid]
    
    def mode(self):
        freq = {}
        for item in self.data:
            freq[item] = freq.get(item, 0) + 1
        max_count = max(freq.values())
        mode_value = [k for k, v in freq.items() if v == max_count]
        return (mode_value[0], max_count)
    
    def var(self):
        mean = self.mean()
        variance = sum((x - mean) ** 2 for x in self.data) / self.count()
        return round(variance, 1)
    
    def std(self):
        return round(self.var() ** 0.5, 1)
    
    def freq_dist(self):
        freq = {}
        for item in self.data:
            freq[item] = freq.get(item, 0) + 1
        
        return sorted([(v * 100 / self.count(), k) for k, v in freq.items()], reverse=True)
    
    def describe(self):
        print('Count:', self.count())
        print('Sum: ', self.sum())
        print('Min: ', self.min())
        print('Max: ', self.max())
        print('Range: ', self.range())
        print('Mean: ', self.mean())
        print('Median: ', self.median())
        print('Mode: ', self.mode())
        print('Variance: ', self.var())
        print('Standard Deviation: ', self.std())
        print('Frequency Distribution:', self.freq_dist())

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)

print('Count:', data.count())  
print('Sum: ', data.sum())    
print('Min: ', data.min())   
print('Max: ', data.max())    
print('Range: ', data.range()) 
print('Mean: ', data.mean())  
print('Median: ', data.median())  
print('Mode: ', data.mode()) 
print('Standard Deviation: ', data.std())
print('Variance: ', data.var())   
print('Frequency Distribution: ', data.freq_dist())

print('\nDescriptive Statistics:')
data.describe()