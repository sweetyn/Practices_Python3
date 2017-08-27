"""Find the maximum consecutive 1's in an array of 0's and 1's.
Example:
a) 00110001001110 - Output :3 [Max num of consecutive 1's is 3]
b) 1000010001 - Output :1 [Max num of consecutive 1's is 1]"""

def maxConsec(givenNum):

    conNum = 0
    maxNum = 0
    preNum = False

    #for i in givenNum:
    #    arr.append(i)
    arr = tuple(givenNum)

    if '1' in arr:
        for x in arr:

            if x == '1' and preNum == True :
                conNum += 1
                preNum = True

            elif x == '1':
                conNum = 1
                preNum = True
            else:
                preNum = False

            if conNum >= maxNum:
                maxNum = conNum

    else:
        print ("There is no 1.")

    return maxNum

givenNum='0011111000110011110'
arr=[]

print('Max num of consecutive 1\'s is ', maxConsec(givenNum))
