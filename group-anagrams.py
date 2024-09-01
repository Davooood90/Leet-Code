class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}

        for i in strs:
            key = "".join(sorted(i))
            if key in dictionary:
                dictionary[key].append(i)
            else:
                dictionary[key] = [i]

        answer = []

        for i, j in dictionary.items():
            answer.append(j)

        return answer