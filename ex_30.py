"""Find the given doubly linked list is palindrome or not.

isPalindrome(new LinkedList().fillData("lol"))
!isPalindrome(new LinkedList().fillData("nottrue"))"""

def checkPalindrome(str1):

    for i in range(int(len(str1)/2)):
        if str1[i] == str1[len(str1)-i-1]:
            continue
        else:
            return False

    return True

str1 = "nottrue"

print (checkPalindrome(str1))
# complted in 6mins
