class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        our_record={}

        for i,n in enumerate(nums):
            diff= target-nums[i]

            if diff in our_record:
                return [our_record[diff],i]
            our_record[n] = i
