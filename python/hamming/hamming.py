__author__ = 'aadil'

def distance(first, second):
    length = len(first)
    first = list(first)
    second = list(second)
    count = 0
    for i in range(length):
        if first[i] != second[i]:
            count+=1
    return count
