"""##NEVER SKIP THIS QUESTION..ASKED IN AMAZON###
Take THREE arrays,like
arr1={1,3,5,7,9};
arr2={1,2,3,5,4,1,8,9,7};
arr3={1,3,5,7,9,2,1,4,6,5,8};
Now find out the Duplicates of First two(arr1,arr2) arrays
and store it in new another array arr4(should contain only duplicates,no unique elements).
Now compare arr3 with arr4.
You should return only UNIQUE elements from both of the array.
If found, return it, else return -1."""

def unique_element(arr1, arr2, arr3):

    arr4 = []
    arr5 = []
    # for x in arr1:
    #     if x in arr2:
    #         arr4.append(x)
    #
    # for y in arr3:
    #     if y in arr4:
    #         continue
    #     else:
    #         arr5.append(y)

# Option2
    print(arr1.intersection(arr2))
    # arr5 = (arr3 - arr4) + (arr4 - arr3)

    if len(arr5) == 0:
        return -1
    else:
        return arr5


arr1 = [1,3,5,7,9]
arr2 = [1,2,3,5,4,1,8,9,7]
arr3 = [1,3,5,7,9,1,5]

print (unique_element(arr1, arr2, arr3))
#completed in 11mins
