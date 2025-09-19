
nums = [-2,1,-3,4,-1,2,1,-5,4]

current_sum = nums[0]
max_sum = nums[0]

for n in nums[1:]:
    current_sum = max(n, current_sum + n)
    max_sum = max(max_sum, current_sum)

print(max_sum)