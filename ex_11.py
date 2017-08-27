"""'aabcbcbdcc' you can remove and shuffle characters,
find the maximum length of string which forms palindrome.
like 'ccabdbacc'"""


def palWord(word):

    chars = list(word)
    counts = dict()
    temWord = ""
    theWord =[]
    result = ""

    #make a diction for counting letters
    for char in chars:
        counts[char] = counts.get(char,0) + 1

    #check the letters even or odd
    odd = ""
    for char, count in counts.items():

        #make even of odd letters except first odd letter
        if count % 2 != 0 and odd == "":
            odd = char
        elif count % 2 != 0:
            counts[char] = counts[char] - 1

    print (counts)
    print (odd)

    for char, count in counts.items():

        if char == odd :
            temWord = char * count
            theWord.insert(int(len(theWord)/2),temWord)
        elif count ==0:
            continue
        else :
            temWord = char * int((count / 2))
            theWord.insert(0,temWord)
            theWord.append(temWord)

    for x in theWord:
        result += x

    return result


word = "aabcbcbdcc"
result = ""

print(palWord(word))
