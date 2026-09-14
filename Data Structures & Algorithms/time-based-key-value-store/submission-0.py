class TimeMap:

    def __init__(self):
        self.store=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        value=self.store[key]
        left=0
        right=len(value)-1
        result= ""
        while left<=right:
            mid = (left+right)//2
            if value[mid][0]<=timestamp:
                result=value[mid][1]
                left=mid+1
            else:
                right=mid-1
        return result
