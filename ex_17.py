"""Given a string and two words which are present in the string,
find the minimum distance between the words
Eg:
"the brown qucik frog quick the", "the", "quick" :O/P -> 1
"the quick the brown quick brown the frog", "the", "the" :O/P -> 2"""

def minDistance(aStr, word1, word2):

    index1 = -1
    index2 = -1
    minDis = len(aStr)

    for i, word in enumerate(aStr.split()):

        #if word1 and wor2 is same
        if word1 == word2 and word1 == word:
            #if index1 get any data yet
            if index1 == -1:
                index1 = i
            #if index1 has a value
            else:
                index2 = i
                if minDis > abs(index2 - index1):
                    minDis = abs(index2 - index1)
                index1 = index2
        #if word1 and word2 is not same
        elif word1 != word2:
            if word ==  word1:
                index1 = i
            elif word == word2:
                index2 = i
            if minDis > abs(index1 - index2):
                minDis = abs(index1 - index2)

    return minDis

print (minDistance("the quick the brown quick brown the frog", "the", "the"))
# Completed



# Other Solution
# def dist(str,s1,s2):
# 	val1, val2 = [], []
# 	i = 0
# 	for x in str.split():
# 		if (s1 == x):
# 			val1.append(i)
# 		if (s2 == x):
# 			val2.append(i)
# 		i += 1
# 	result = [abs(x-y) for x in val1 for y in val2]
# 	if (s1 == s2):
# 		result = [abs (x - y) for x in val1 for y in val1 if (x!=y)]
# 	if result:
# 		return min(result)
# 	return 0
#
# print(dist("the quick the brown quick brown the frog", "the", "the"))
