import itertools
from math import factorial

def itertools_permutations(itr, r=None):
    return itertools.permutations(itr, r)

def lexicographical_1(itr, r=None):
    seq = list(itr)
    n = len(itr) if r is None else r
    indices = [i for i in range(n)]

    yield tuple(seq[index] for index in indices)

    while True:
        i = n -1
        while i > 0 and indices[i - 1] >= indices[i]:
            i -= 1
        if i == 0:
            return

        # find the smallest item in the suffix, that is bigger than the pivot
        j = len(indices) - 1
        while indices[j] <= indices[i - 1]:
            j -= 1

        x = i - 1  # item immediately before suffix, called pivot
        indices[x], indices[j] = indices[j], indices[x]  # swap pivot with item found in suffix
        indices[i:] = indices[len(indices) - 1: i - 1: -1]  # reverse the suffix for the next smallest value in the sequence

        yield tuple(seq[index] for index in indices)

def plain_changes(itr):
    seq = list(itr)
    n = len(seq)
    a = generate(n, itr)
    return list(a)

def exch(lst, i, j):
    # print("\t", lst ,i, j)
    lst[i], lst[j] = lst[j], lst[i]

def generate(n, lst):
    if n == 1:
        yield lst
    c = 0
    while c < n - 1:
        exch(lst, c, n - 1)
        generate(n - 1, lst)
        exch(lst, c, n-1)
        c += 1
    generate(n - 1, lst)


if __name__ == "__main__":
    # a = itertools_permutations([1, 2, 3, 4])
    # b = lexicographical_1([1, 2, 3, 4])
    # for i, j in zip(a, b):
    #     print(i, j)
    a = plain_changes([1,2,3])
    print(a)