class Solution(object):
    def removeDuplicates(self, nums):
        answer =1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[answer] = nums[i]
                answer += 1
        return answer
