class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = 0
        double = 0
        total = sum(nums)

        for num in nums:
            if num < 10:
                single += num
            elif num < 100:
                double += num

        return single > total - single or double > total - double