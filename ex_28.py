"""Given a Integer, find the maximum number that can be formed from the digits.
Input : 8754365
output : 8765543

I told solution in nlogn. He asked me optimize further.
"""


def max_num(aInt):

    result = []
    tem_str = ""
    tem_str = str(aInt)

    for x in tem_str:
        result.append(x)

    print (result)
    result.sort()
    result.reverse()

    tem_str = ""
    for x in result:
        tem_str += x

    return tem_str

aInt = 8754365

print (max_num(aInt))
# complted in 18 mins
