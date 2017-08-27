"""You are given an array of integers. Find the minimum difference
between two prime numbers(Positive or negative) in the array
when present with minimum time complexity
and provide the test data to test the this code."""

def minDiffVal(primeNum):
    minVal = max(primeNum)

    for i in range(len(primeNum)-1):
        curVal = primeNum[i+1] - primeNum[i]
        if curVal < minVal:
            minVal = curVal

    return minVal


def minDiffPrime(arr):

    #remove negative numbers, 0 and 1
    arr = sorted(list(filter(lambda x: x>1, arr)))
    print(arr)


    #find prime numbers
    for x in arr:
        j=2
        flag = False

        while x >= j and flag == False:
            print('x=',x,' j=',j)
            if x%j==0 and x==j:
                flag = True
                primeNum.append(j)
                print('x=',x,' j=',j, 'prime')
            elif x%j==0:
                flag = False
                break
            j += 1

    print(primeNum)

    if not len(primeNum) == 0:
        result = minDiffVal(primeNum)
    else:
        print("There is no Prime Numbers")
        result = primeNum

    return result


arr = [3,37,5,27,7,64,1,22,11,13]
primeNum=[]


print(minDiffPrime(arr))
