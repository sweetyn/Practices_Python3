"""Give this
input: Sea!tle is a nice place. Work Hard! have Fun, make HIStory!
display this output using any C or vb script:

output :
Seattle is a nice place.
Work hard.
Have fun.
Make history."""

def org_text(str1):

    result = ""

    result = str1.replace("!", "t", 1)
    result = result.replace(". ", ".\n")
    result = result.replace("! ", ".\n")
    result = result.replace(", ", ".\n")
    result = result.replace("!", ".\n")

    for sen1 in result.splitlines():
        result += sen1.capitalize()

    return result

str1 = "Sea!tle is a nice place. Work Hard! have Fun, make HIStory! "

print (org_text(str1))
#complted in 1hour and 16mins
