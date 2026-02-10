class TimeMap:

    def __init__(self):
        self.key_map = {} # value being a list of (value, timestamp) pair 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_map:
            self.key_map[key] = []
        # since input guarantees timestamp strictly increasing, simple append
        self.key_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        result, value_pairs = "", self.key_map.get(key, [])
        left, right = 0, len(value_pairs) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if timestamp >= value_pairs[mid][1]:
                result = value_pairs[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)