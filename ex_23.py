"""Find the max consecutive repitative chracter

A = "ffgggtvshjsdhjfffffffhvjbjcharu"
Output : f -> 7
"""

def maxConsChra(str1):

    temp = dict()
    aString[] = list(str1)
    maxNum = 0
    char = ''
    result = ''

    for x in aString:
        temp[x] = temp.get(x,0) + 1

    for key, val in temp.items():
        if val > maxNum:
            maxNum = val
            char = key

    # result = str(maxNum)
    result = char + " -> " + str(maxNum)
    print (char, " -> " ,maxNum)



str1 = "ffgggtvshjsdhjfffffffhvjbjcharu"

print (maxConsChra(str))
