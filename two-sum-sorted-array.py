class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        bot = 0
        top = len(numbers) - 1

        while bot < top:
            answer = numbers[bot] + numbers[top]
            if answer < target:
                bot += 1
            elif answer > target:
                top -= 1
            else:
                return [bot + 1, top + 1]