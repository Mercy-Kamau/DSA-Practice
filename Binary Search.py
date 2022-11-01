
nums = [-1,0,3,5,9,12]
target = 9
class Solution:
    def search( nums, target):
        left_pointer = 0
        right_pointer = len(nums)-1 #last index length of array - 1
        while left_pointer <= right_pointer: #shows no more possibilities left or target is found
            midpoint = (left_pointer + right_pointer) // 2
            if nums[midpoint] > target:
                right_pointer = midpoint - 1 #look values to left to shrink criteria
            elif nums[midpoint] < target:
                left_pointer = midpoint + 1
            else:
                return midpoint #meaning its equal to the target
        return -1
    result = search(nums, target)
    print(result)





