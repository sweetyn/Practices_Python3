"""Given two sorted lists and an integer k, merge the lists up to a maximum of k elements.
print(merge_k(4, [1,2,3,4], [2,3,4,5]))  #[1, 2, 2, 3]
print(merge_k(8, [1,2,3,4], [2,3,4,5]))  #[1, 2, 2, 3, 3, 4, 4, 5]
print(merge_k(15, [1,2,3,4], [2,3,4,5])) #[1, 2, 2, 3, 3, 4, 4, 5]
print(merge_k(15, [1], [2,3,4,5]))       #[1, 2, 3, 4, 5]"""


def merge_k(k, list1, list2):

    merged = []
    result = []
    i = 0

    merged = list1 + list2
    merged.sort()

    if k > len(merged):
        result = merged[:]
    else:
        result = merged[:k]

    return result

print (merge_k(8, [1,2,3,4], [2,3,4,5]))
# complted in 10mins
