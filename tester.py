import itertools
import timeit
import random

class Generator(object):
    def itertools_permutations(self, itr, r=None):
        # Return successive r length permutations of elements in the iterable.
        return itertools.permutations(itr, r)

    def itertools_permutations_time(self, itr, r=None):
        # Return the time taken to generate successive r length permutations of elements in the iterable.
        return timeit.timeit(lambda: list(self.itertools_permutations(itr, r)), number=10000)

    def permutations(self, itr):  #TODO update to work based on indexes
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

    def permutations_time(self, itr):
        return timeit.timeit(lambda: list(self.permutations(itr)), number=10000)

    def itertools_combinations(self, itr, r):
        return itertools.combinations(itr, r)

    def itertools_combinations_time(self, itr, r):
        return timeit.timeit(lambda: list(self.itertools_combinations(itr, r)), number=10000)

    def itertools_combinations_with_replacement(self, itr, r):
        return itertools.combinations_with_replacement(itr, r)

    def itertools_combinations_with_replacement_time(self, itr, r):
        return timeit.timeit(lambda: list(self.itertools_combinations_with_replacement(itr, r)), number=10000)

    def combinations(self, itr, r):
        indices = [0 for i in range(r)]
        length = len(itr)

        while sum(indices) != ((length - 1) * len(indices)):
            curr_index = len(indices) - 1
            while True:
                indices[curr_index] += 1
                if indices[curr_index] >= length:
                    indices[curr_index] = 0
                    curr_index -= 1
                else:
                    i = curr_index
                    while i <= len(indices) - 1:
                        indices[i] = indices[curr_index]
                        i += 1
                    break
            if len(indices) == len(set(indices)):
                yield tuple(itr[index] for index in indices)

    def combinations_with_replacement(self, itr, r):
        indices = [0 for i in range(r)]
        length = len(itr)

        yield tuple(itr[index] for index in indices)

        while sum(indices) != ((length - 1) * len(indices)):
            curr_index = len(indices) - 1
            while True:
                indices[curr_index] += 1
                if indices[curr_index] >= length:
                    indices[curr_index] = 0
                    curr_index -= 1
                else:
                    i = curr_index
                    while i <= len(indices) - 1:
                        indices[i] = indices[curr_index]
                        i += 1
                    break
            # print(indices)
            yield tuple(itr[index] for index in indices)

    def combinations_with_replacement_time(self, itr, r):
        return timeit.timeit(lambda: list(self.combinations_with_replacement(itr, r)), number=10000)

    def random_permutation(self, itr):
        itr = list(itr)
        n = len(itr) - 1
        i = 0
        while i < n:
            rand_num = random.randint(i, n)
            itr[i], itr[rand_num] = itr[rand_num], itr[i]
            i += 1
        return itr

if __name__ == "__main__":
    g = Generator()
    # a = list(g.combinations([1,2,3,4], 2))
    # a = list(g.default_comb([3,2,1,1], 2))
    # for i in a:
    #     print(i)
    # print(g.comb_with_replacement_time([1,2,3,4], 3))
    # print(g.default_comb_with_replacement_time([1,2,3,4], 3))
    # print("\n")
    # a = list(g.default_comb_with_replacement([3,2,1,1], 2))
    # for i in a:
    #     print(i)
    # test([1,2,3,4])
    # print("Default time (5 values) = ", g.default_perm_time(range(5)))
    # print("Lex_gen time (5 values) = ", g.lex_gen_time(range(5)))
    # print("Default time (3 values) = ", g.default_perm_time([3,2,1]))
    # print("Lex_gen time (3 values) = ", g.lex_gen_time([3,2,1]))
    print(g.random_permutation(range(6)))
