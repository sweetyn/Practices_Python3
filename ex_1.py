"""####LAB126
#Write a funcion and return the index of the first occurrence of a substring in a string

def parse_substring(str1, str2):
    for x in range(len(str1)):
        if str2 in str1[x:x+(len(str2))]:
            x = str1.find(str2)
            return x

print (parse_substring("I am a student", "am"))
print (parse_substring("I am a student", "I am a student....."))

Test this function:
"""


def parse_substring(str1, str2):
    x = str1.find(str2)
    return x

print (parse_substring("I am a student", "am"))
print (parse_substring("I am a student", "student"))

#
# """ Test case for this function:
# 1) input can be various types
# print (parse_substring("I am a student", 123))
# Expected result: -1
#
# 2) input can be longer string than orginal sentence
# print (parse_substring("I am a student", "I am a student….."))
# Expected result: -1
# """
