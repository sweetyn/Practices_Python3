"""###LAB126
Write a funcion and return the index of the first occurrence of a substring in a string

string1 = "Test1, test2, test3, test4, Test5, test6"

    print '"test" occurs %d times in \n\t%s' % \
        ( string1.count( "test" ), string1 )
    print '"test" occurs %d times after 18th character in \n\t%s' % \
        ( string1.count( "test", 18, len( string1 ) ), string1 )


Test this function:
"""

def parse_substring():
    string1 = "Test1, test2, test3, test4, Test5, test6"

    print '"test" occurs %d times in \n\t%s' % ( string1.count( "test" ), string1 )
    print '"test" occurs %d times after 18th character in \n\t%s' % \
        ( string1.count( "test", 18, len( string1 ) ), string1 )
    return ""

# print (parse_substring())
parse_substring()
