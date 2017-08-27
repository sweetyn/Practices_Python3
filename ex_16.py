"""Given a string, calculate the frequency of characters,
output the array with the letter and frequency.
(such as: for “abbcdc”, the output should be (a,1),(b,2),(c,2),(d,1))
"""

# stringChars = list('abbcdc')
# print(list({key: stringChars.count(key) for key in stringChars}.items()))

def frequenChars(aStr):

    aDict = dict()

    for x in aStr:
        aDict[x] = aDict.get(x,0) + 1

    return list(aDict.items())

aStr = 'abbcdc'

print (frequenChars(aStr))
