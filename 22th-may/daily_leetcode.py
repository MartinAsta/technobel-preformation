'''There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
'''
def search(nums: list, target: int) -> int:
        if target not in nums:
            return -1
        elif target == nums[0]:
            return 0
        elif target == nums[1]:
            return 1
        
        pivot = 0
        left = 1
        right = len(nums) - 1
        mid = ((right - left) // 2) + left
        while left < right:
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[mid - 1]:
                left = right + 1
                pivot = mid
            elif nums[mid] < nums[right]: #right is sorted
                right = mid
                mid = ((right - left) // 2) + left
            else: #left is sorted
                left = mid
                mid = ((right - left) // 2) + left
            if nums[mid] == target:
                return mid
            if mid + 1 == right:
                left = right + 1
                pivot = right
        print(pivot)
        if target >= nums[pivot] and target <= nums[-1]:
            left = pivot
            right = len(nums)-1
        else:
            right = pivot
            left = 0
        mid = ((right - left) // 2) + left
        if nums[mid] == target:
            return mid
        while left < right:
            if target > nums[mid]:
                left = mid
                mid = ((right - left) // 2) + left + 1
            else:
                right = mid
                mid = ((right - left) // 2) + left
            if nums[mid] == target:
                return mid

arr = [2,4,7,9,0]
print(search(arr,9))