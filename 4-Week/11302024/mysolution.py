class TimeMap: 
    def __init__(self):
        #self.timechecker = dict()# key: timestampe , value: key of hashchecker
        self.hashchecker = collections.defaultdict(list)# key: key, value: val

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.hashchecker:
            self.hashchecker[key] = []
        self.hashchecker[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:  
        if not key in self.hashchecker:
            return ""
        
        left = 0
        right = len(self.hashchecker[key])
        
        while left < right:
            mid = (left + right) // 2
            if self.hashchecker[key][mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid
                
        if right == 0:
            return ""
        return self.hashchecker[key][right - 1][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
