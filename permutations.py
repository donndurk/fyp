import itertools

def itertools_permutations(itr, r=None):
    return itertools.permutations(itr, r)

def permutations(itr):  # TODO update to work based on indexes
    # Lexicographical permutation generator
    seq_length = len(itr)
    seq = list(sorted(itr))  # start with a sorted sequence
    yield seq

    # start looping to generate all permutations
    while True:
        # find longest weakly-decreasing suffix
        i = seq_length - 1

        while i > 0 and seq[i - 1] >= seq[i]:
            i -= 1
        # if i points to the first item, then the sequence has the highest value and is done
        if i == 0:
            return

        # find the smallest item in the suffix, that is bigger than the pivot
        j = len(seq) - 1
        while seq[j] <= seq[i - 1]:
            j -= 1

        x = i - 1  # item immediately before suffix, called pivot
        seq[x], seq[j] = seq[j], seq[x]  # swap pivot with item found in suffix
        seq[i:] = seq[len(seq) - 1: i - 1: -1]  # reverse the suffix for the next smallest value in the sequence

        yield seq

def lex_permutations(itr, r=None):
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

if __name__ == "__main__":
    a = itertools_permutations([1, 2, 3], 3)
    # a = lex_permutations([1,2,3], 1)
    for i in a:
        print(i)