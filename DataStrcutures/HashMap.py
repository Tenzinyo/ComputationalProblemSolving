from collections import defaultdict
class HashMap:
    def groupAnagrams(self, List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        result = []
        for s in strs:
            sorted_list = tuple(sorted(i))
            anagram[sorted_list].append(s)

        for value in anagram.values():
            result.append(value)
            
