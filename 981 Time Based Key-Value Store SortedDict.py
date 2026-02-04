class TimeMap:

    def __init__(self):
        self.f_map = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.f_map[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.f_map:
            return ""
        
        timeStamp_map = self.f_map[key]
        index = timeStamp_map.bisect_right(timestamp) - 1

        if index >= 0:
            closest_ts = timeStamp_map.iloc[index]
            return timeStamp_map[closest_ts]
        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)