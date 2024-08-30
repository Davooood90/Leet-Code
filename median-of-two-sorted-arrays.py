class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        answer = sorted(nums1 + nums2)
        num = len(answer)
        if num % 2 == 0:
            return ((answer[num//2] + answer[num//2 - 1])/2)
        else:
            return answer[num//2]