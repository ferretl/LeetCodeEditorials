def twoSum(nums: list[int], target: int) -> list[int, int]:
    for i in range(len(nums)):
        nums[i] = [nums[i],i]
    nums = sorted(nums, key = lambda x:x[0])
    l,r = 0, len(nums)-1
    while l < r:
        s = nums[l][0] + nums[r][0]
        if s < target:
            l += 1
        elif s > target:
            r -= 1
        else:
            return [nums[l][1], nums[r][1]]
    # by Leetcode specs we won't ever reach here but still good to have
    return [-1,-1]

nums = [1,5,7,2,9]
target = 3
print(twoSum(nums,target))