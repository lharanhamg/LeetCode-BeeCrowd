def rec_bin_search(nums, target, l=0, r=None):

    if r is None:
        r = len(nums) - 1

    m = (l + r) // 2

    if l > r:
        return -1

    if nums[m] == target:
        return m

    elif nums[m] > target:
        return rec_bin_search(nums, target, l=l, r=m-1)
    
    elif nums[m] < target:
        return rec_bin_search(nums, target, l=m+1, r=r)
    
    return rec_bin_search(nums, target)

print(rec_bin_search([1,2,3,4,5,6,7,8,9], 9))