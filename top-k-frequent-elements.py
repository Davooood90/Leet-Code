class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}

        for i in set(nums):
            dictionary[i] = nums.count(i)

        dictionary = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)

        answer = []
        for i in range(k):
            answer.append(dictionary[i][0])

        return answer