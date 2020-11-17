def firstn(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        print(nums)
        num += 1
    return nums

Sum_of_first_n = sum(firstn(10))

print(Sum_of_first_n)