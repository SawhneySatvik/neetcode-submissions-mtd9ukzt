class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            hash_map[key].append(s)

        res = []
        for vals in hash_map.values():
            res.append(vals)

        return res