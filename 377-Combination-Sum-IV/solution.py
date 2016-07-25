class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        combinations = [None] * (target + 1)
        combinations[0] = 1
        return self.combinationAux(nums, target, combinations)
    
    def combinationAux(self, nums, target, combinations):
        if target < 0:
            return 0
        elif combinations[target] != None:
            return combinations[target]
        else:
            combinations[target] =  sum([self.combinationAux(nums, target - nums[i], combinations) for i in range(len(nums))])
            return combinations[target]