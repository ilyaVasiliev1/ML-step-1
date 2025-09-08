nums = [1,1,2]

i = 1 
for j in range(1, len(nums)):
    if nums[j] != nums[i - 1]:
        nums[i] = nums[j]
        i += 1
print(i, nums[:i])