"""Write second most repeating word in a string
eg aaa bbb ccc aaa bbb aaa
answer - bbb"""


def fre_repeating(str1):

    tem_words = []
    con_words = dict()
    sec_val = 0
    sec_key = ''

    #split the given string
    tem_words = str1.split()

    #make a dictionary
    for x in tem_words:
        con_words[x] = con_words.get(x,0)+1

    #find second max value
    for key, val in con_words.items():
        if val < max(con_words.values()) and val > sec_val:
            sec_val = val
            sec_key = key

    return sec_key

str1 = "aaa bbb ccc aaa bbb aaa"

print(fre_repeating(str1))

# complted
