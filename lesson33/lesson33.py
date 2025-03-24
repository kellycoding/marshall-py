nums = [1,2,3,5,6,9,20,40,51,52]

mean = sum(nums)/len(nums)

if len(nums)%2 == 0:
    index1 = len(nums)//2
    index2 = index1 - 1
    median = (nums[index1]+nums[index2])/2
else:
    median = nums[len(nums)//2]

print(f"The mean is {mean} and the median is {median}")