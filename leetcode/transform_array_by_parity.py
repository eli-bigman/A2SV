def transformArray(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = []
    for i in nums:
        if i % 2 == 0:
            res.append(0)
        else:
            res.append(1)
    res.sort()
    return res

print(transformArray([0,1,2,3,4])) # [0,1,0,1,0]