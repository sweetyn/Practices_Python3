"""Find the max poduct value of 3 number from the given array .
For example , if array has [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
find the max product from three numbers. max_product(x*x*x)
Twist is array can contain negative number as well"""

def maxProNumbs(arr):

    temArr = []

    arr.sort()
    if arr[0] and arr[1] < 0:
        temArr.append(arr[0])
        temArr.append(arr[1])

    arr.reverse()
    if arr[0] and arr[1] and arr[2] > 0:
        temArr.append(arr[2])
        temArr.append(arr[1])
        temArr.append(arr[0])

    if len(temArr) > 3:
        if temArr[0] * temArr[1] >= temArr[2] * temArr[3]:
            result = temArr[0] * temArr[1] * temArr[4]
        else:
            result = temArr[2] * temArr[3] * temArr[4]
    else:
        result = temArr[0] * temArr[1] * temArr[2]

    return result

arr = [-161,-1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

print (maxProNumbs(arr))

#Completed!!
