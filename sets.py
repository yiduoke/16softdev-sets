# [2*x for x in range(1,51)]
# [3*x for x in range(1,34)]
# [var1 for var1 in range(2,101) for var2 in range (2, var1) if var1%var2==0]


def intersection(set1, set2):
    return [x for x in set1 if x in set1 and x in set2]

# print intersection({1, 2, 3}, {2, 3, 4})

def difference(set1, set2):
    return [x for x in set1 if x in set1 and x not in set2]

def symmetric_diff(set1, set2):
    return union(difference(set1, set2), difference(set2, set1))

def union(set1, set2):
    return intersection(set1, set2) + difference(set1, set2) + difference(set2, set1)

print union({1, 2, 3}, {2, 3, 4})
# print difference({1, 2, 3}, {2, 3, 4})