import itertools
import timeit

class Generator(object):
    def default_perm(self, itr, r=None):
        # Return successive r length permutations of elements in the iterable.
        return itertools.permutations(itr, r)

    def default_perm_time(self, itr, r=None):
        # Return the time taken to generate successive r length permutations of elements in the iterable.
        return timeit.timeit(lambda: list(self.default_perm(itr, r)), number=10000)

    def lex_gen(self, itr):
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

    def lex_gen_time(self, itr):
        return timeit.timeit(lambda: list(self.lex_gen(itr)), number=10000)

    def default_comb(self, itr, r):
        return itertools.combinations(itr, r)

    def default_comb_time(self, itr, r):
        return timeit.timeit(lambda: list(self.default_comb(itr, r)), number=10000)

    def default_comb_with_replacement(self, itr, r):
        return itertools.combinations_with_replacement(itr, r)

    def default_comb_with_replacement_time(self, itr, r):
        return timeit.timeit(lambda: list(self.default_comb_with_replacement(itr, r)), number=10000)

    def comb_with_replacement(self, itr, r):
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
                    break
            yield tuple(itr[index] for index in indices)

    def comb_with_replacement_time(self, itr, r):
        return timeit.timeit(lambda: list(self.comb_with_replacement(itr, r)), number=10000)

if __name__ == "__main__":
    g = Generator()
    a = list(g.comb_with_replacement([1,2,3,], 2))
    # a = list(g.default_comb([3,2,1,1], 2))
    for i in a:
        print(i)
    print(g.comb_with_replacement_time([1,2,3,4], 3))
    print(g.default_comb_with_replacement_time([1,2,3,4], 3))
    # print("\n")
    # a = list(g.default_comb_with_replacement([3,2,1,1], 2))
    # for i in a:
    #     print(i)
    # test([1,2,3,4])
    # print("Default time (5 values) = ", g.default_perm_time(range(5)))
    # print("Lex_gen time (5 values) = ", g.lex_gen_time(range(5)))
    # print("Default time (3 values) = ", g.default_perm_time([3,2,1]))
    # print("Lex_gen time (3 values) = ", g.lex_gen_time([3,2,1]))
