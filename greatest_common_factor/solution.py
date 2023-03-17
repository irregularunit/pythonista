def greatest_common_factor(nums):
    smallest = min(nums)
    for i in range(smallest, 0, -1):
        for num in nums:
            if num % i != 0:
                break
        else:
            return i
