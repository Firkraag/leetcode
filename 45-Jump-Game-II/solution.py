class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return 0
        lastTrue = n - 1
        jumps = [0] * n
        indices = range(n)
        for i in range(n - 2, -1, -1):
            step = nums[i]
            if i + step >= n - 1:
                jumps[i] = 1
                lastTrue = i
                indices[i] = n - 1
            elif i + step >= lastTrue:
                index = lastTrue
                while True:
                    #if i == 0:
                     #   print i, step, index, jumps[index] 
                    if index <= i + step and i + step < indices[index]:
                        jumps[i] = jumps[index] + 1
                        lastTrue = i
                        indices[i] = index
                        break
                    else:
                        index = indices[index]
            #print jumps, indices, lastTrue
        return jumps[0]