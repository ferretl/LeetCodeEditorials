def longestConsecutive(nums: list[int]) -> int:
    nums = set(nums)
    largestSeq = 0
    for num in nums:
        if num - 1 not in nums:
            count = 1
            while num + 1 in nums:
                count += 1
                num += 1
            largestSeq = max(largestSeq, count)
    return largestSeq

