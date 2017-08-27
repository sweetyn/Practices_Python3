"""Print the count of duplicate char in a given string in same order.
Ex: Input- 'abbaccdbac', Output- 'a3b3c3d1' """


def coutDupChar(word):

    tempWord = list(word)
    temDic = dict()
    result = ""

    for x in tempWord:
        temDic[x] = temDic.get(x, 0)+1

    for char, val in temDic.items():
        result += char + str(val)

    return result

word = 'abbaccdbac'

print (coutDupChar(word))
# complted
