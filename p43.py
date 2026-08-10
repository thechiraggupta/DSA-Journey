def threeSumClosest(nums, target):
    nums.sort()
    n = len(nums)
    
    closest = nums[0] + nums[1] + nums[2]

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current = nums[i] + nums[left] + nums[right]

            # Update closest sum
            if abs(current - target) < abs(closest - target):
                closest = current

            # Exact match
            if current == target:
                return current

            # Move pointers
            if current < target:
                left += 1
            else:
                right -= 1

    return closest