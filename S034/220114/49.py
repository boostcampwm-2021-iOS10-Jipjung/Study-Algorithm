from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for string in strs:
            key = "".join(sorted(string))
            anagrams[key].append(string)
        return anagrams.values()
        