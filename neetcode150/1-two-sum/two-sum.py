class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res={}
        for i in range(len(nums)):
            reqd=target-nums[i]
            if reqd in res:
                return(res[reqd],i)
            res[nums[i]]=i
            