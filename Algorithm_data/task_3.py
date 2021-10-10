
## using Binary search
def get_index(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    if low == len(nums):
        return len(nums)
    elif high < 0:
        return 0
    else:
        return low
    

nums = [1,3,5,6]
target = 4

print(get_index(nums, target))

### Time Complexity if Binary Search is O(log n)
### Space Complexity is O(1) constant
