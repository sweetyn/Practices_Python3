"""Given a number in an array form. Write a program to move all zeros to the end.
Input :  arr[] = {1, 2, 0, 4, 3, 0, 5, 0};
Output : arr[] = {1, 2, 4, 3, 5, 0, 0};

Input : arr[]  = {1, 2, 0, 0, 0, 3, 6};
Output : arr[] = {1, 2, 3, 6, 0, 0, 0};"""


def moveZros(arr):

    temp1 = []
    temp2 = []
    result = []

    for x in arr:
        if x == 0:
            temp2.append(x)
        else:
            temp1.append(x)

    result = temp1+temp2

    return result

arr = [1, 2, 0, 0, 0, 3, 6]

print(moveZros(arr))
