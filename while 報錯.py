nums: List[int]
j = 0
n = len(nums)

while nums[j] and j < n:
    j += 1
报错：IndexError: list index out of range

while j < n and nums[j]:
    j += 1
无报错，因为先判断 j < n
