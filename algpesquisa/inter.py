def interpolacao(nums, target):
    l = 0
    r = len(nums) - 1
    mid = int(l + ((r - l) // (nums[r] - nums[l]) * (target - nums[l])))
    if nums[mid] == target:
        return mid

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(nums)
target = 4
print(interpolacao(nums,target))
