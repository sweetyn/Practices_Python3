"""Replace %20 with ' '.
E.g. input: www.space%20.com
output: www.space .com"""


def replace_word(str1):

    result = ""
    i=0
    if "%20" in str1:

        for i in range(len(str1)):
            if str1[i:i+3] =="%20":
                result = str1[:i] + " " + str1[i+3:]

    return result

str1 = "www.space%20.com"

print (replace_word(str1))
# complted in 6mins
