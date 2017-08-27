"""'aabcbcbdcc' you can remove and shuffle characters,
find the maximum length of string which forms palindrome.
like 'ccabdbacc'"""

def palWord(word):

    temWord = list(word)
    theWord = ""
    addWord = ""
    odd = False
    location =0

    for char in temWord:

        if char not in theWord:
            if temWord.count(char) % 2 !=0 and odd == False:
                addWord = char * temWord.count(char)
                location = int(len(theWord)/2)
                theWord = theWord[:location] + addWord + theWord[location:]
                odd = True
            else:
                addWord = char * int(temWord.count(char) / 2)
                theWord = addWord + theWord + addWord

    return theWord


word = "aabcbcbdcc"

print(palWord(word))
