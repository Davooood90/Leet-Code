class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(set(nums))
        answer = 1
        count = 1

        prev = nums[0]

        for i in nums[1:]:
            if i - 1 == prev:
                count += 1
            else:
                answer = max(count, answer)
                count = 1
            prev = i
        return max(count, answer)