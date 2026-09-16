class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outputs = []
        map_sets = {}
        for i in strs:
            curr_list = tuple(sorted(i))
            map_sets.setdefault(curr_list, []).append(i)
        for j in map_sets:
            outputs.append(map_sets[j])
        return outputs
        