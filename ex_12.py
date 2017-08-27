"""Write a program to diplay a character occurred maximum times and if
two charaters occurring same no of times then display 1st character in string.
"HELLO WORLD!" display L
"HO HELLO!" display H (H, L and O appeared 2 times but H is in 1st in string)"""


def maxOccChar(sen):

    occChar = dict()
    result = ''

    for x in sen:
        occChar[x] = occChar.get(x,0) + 1

    maximum = max(occChar.values())
    print("maximum: ",maximum )
    for key, index in occChar.items():
        if maximum == index and result == '':
            result = key

    return result

sen = "HHHELLO WORLD!"

print(maxOccChar(sen))
# Completed
