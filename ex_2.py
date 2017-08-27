"""
Write the test cases for below logic.
i/p: string, strong
o/p: strng
"""

def parse_sameString(str1, str2):
    output =""
#    for x in range(len(str1)):
#        if str1[x] in str2:
#            output += str1[x]
    for x in str1:
        if x in str2:
            output += x
    return output

print(parse_sameString("string","strong"))


"""
1. f (string, strong) // happy path
2. f (null, null) // both null
3. f ("", "") // both empty strings
4. f (" ", " ") // both empty strings with spaces - blank strings
5. f ("abc", "zxy") // no matches
6. f ("!@#$", "1@#!@") // special chars
7. f (null, "somestring") // 1st param null other not
8. f ("somestring", null) // 2nd param null other not
9. Test with very large inputs
10. f ("azzzzzzzz", "zzzzzzza") // mathcing in different positions

In general terms these are some sample test cases to begin with, but
other tests that could be included as necessary.

"""
