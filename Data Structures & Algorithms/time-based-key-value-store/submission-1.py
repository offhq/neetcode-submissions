class TimeMap:

    def __init__(self):
        self.di = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.di:
            self.di[key] = []
        self.di[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.di:
            n = len(self.di[key])
            arr = self.di[key]
            low = 0
            high = n -1
            ans = ""
            while low <= high:
                mid = low + (high-low) // 2
                if arr[mid][1] == timestamp:
                    ans = arr[mid][0]
                    break
                elif arr[mid][1] < timestamp:
                    ans = arr[mid][0]
                    low = mid + 1
                else:
                    high = mid -1
            return ans
        else:
            return ""


