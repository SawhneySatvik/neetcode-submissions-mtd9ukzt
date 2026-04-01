class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key][0].append(value)
            self.data[key][1].append(timestamp)
        else:
            self.data[key] = [[value], [timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.data:
            vals = self.data[key][0]
            time = self.data[key][1]

            low, high = 0, len(time) - 1
            ans = ""
            while low <= high:
                mid = (low+high)//2
                if time[mid] <= timestamp:
                    ans = vals[mid]
                    low = mid + 1
                else:
                    high = mid - 1

            return ans

        else:
            return ""