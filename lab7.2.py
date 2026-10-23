def combination_sum2(candidates, target ):
    nums= sorted(candidates)
    result = []
    current = []

    def backtrack(start, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            if nums[i] > remaining:
                break
            current.append(nums[i])
            backtrack(i + 1, remaining - nums[i])
            current.pop()
    backtrack(0, target)
    return result

print(combination_sum2([10, 1, 2, 7, 6, 1, 5], 8))
print(combination_sum2([2, 5, 2, 1, 2], 5))
