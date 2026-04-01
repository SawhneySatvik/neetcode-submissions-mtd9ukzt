class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0]*26
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        
        max_freq = max(count)

        ele_with_max_freq = 0
        for freq in count:
            if freq == max_freq:
                ele_with_max_freq += 1
        
        return max(len(tasks), ((max_freq-1)*(n+1)+ele_with_max_freq))