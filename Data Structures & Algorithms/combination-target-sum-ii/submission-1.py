class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()

        def dfs(i, total, path):
            if total == target:
                res.add(tuple(path.copy()))
                return
            
            if i >= len(candidates) or total > target:
                return
            
            path.append(candidates[i])
            dfs(i+1, total+candidates[i], path)

            path.pop()
            dfs(i+1, total, path)
        
        dfs(0, 0, [])
        return [list(tup) for tup in res]