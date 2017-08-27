"""Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]."""


def two_sum(arr1, target):

    result = []
    count = 0

    for x in arr1:

        i = 1 + count

        while i < len(arr1):

            if target == x + arr1[i]:
                result.append(arr1.index(x))
                result.append(i)
                return result

            i += 1

            if i == len(arr1):
                count += 1

    return False

arr1 = [11, 5, 7, 3, 15]
target = 10

print (two_sum(arr1, target))

#compldted in 14mins
