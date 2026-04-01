class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(index, path):
            if index == len(s):
                res.append(path[:])
                return

            for i in range(index, len(s)):
                if self.isPalindrome(s[index:i+1]):
                    path.append(s[index:i+1])
                    backtrack(i+1, path)
                    path.pop()

        backtrack(0, [])
        return res