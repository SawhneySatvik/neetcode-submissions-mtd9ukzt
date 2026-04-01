class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []

        def backtrack(i: int, path: str) -> None:
            if i >= len(digits):
                res.append(path)
                return
            
            for char in mapping[int(digits[i])]:
                backtrack(i+1, path+char)
        
        backtrack(0, "")
        return res