"""find first not-repeating character by iterating
through the length of the string only once and by using constant space."""

def first_non_repeat(str1):

    i = 0

    for x in str1:
        i += 1
        if x in str1[i:]:
            continue
        else:
            return x


str1 = "azaasaxbbbbacccdbbbbeeeg"

print (first_non_repeat(str1))
# complted in 18mins
