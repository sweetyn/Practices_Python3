"""check if the string is palindrome
ex:- PooP, madAM, mom
"""

def checkPalindrome(aWord):

    i = 0

    while i < len(aWord)/2:
        if aWord[i].upper() == aWord[len(aWord)-i-1].upper():
            result = True
        else:
            result = False
            break
        i += 1

    return result

aWord = "PooP"

print(checkPalindrome(aWord))
