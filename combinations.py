import random

def algorithm_L(itr, t):
    counter = 0
    seq = list(itr)
    #l1
    c = [j for j in range(t)]
    c.append(len(seq))
    c.append(0)
    # c = c[::-1]
    while True:
        #l2
        counter += 1
        # print(c[:-2][::-1])
        print(list(seq[i] for i in c[:-2]))
        #l3
        j = 1
        while c[j-1] + 1 == c[j+1-1]:
            c[j-1] = j - 1
            j += 1
        #l4
        if j > t:
            print(counter)
            return
        #l5
        c[j-1] += 1

def algorithm_T(itr, t):
    counter = 0
    seq = list(itr)
    # t1
    c = [j for j in range(t)]
    c.append(len(seq))
    c.append(0)
    # c = c[::-1]
    j = t-1
    while True:
        #t2
        counter += 1
        print(list(seq[i] for i in c[:-2]))
        # print(list(seq[i] for i in c[2:]))
        if j > 0:
            x = j
            #t6
            c[j-1] = x
            j -= 1
            continue
        #t3
        if c[0]+1 < c[1]:
            c[0] += 1
            continue
        else:
            j = 2
        #t4
        c[j-2] = j - 3
        x = c[j-1] + 1
        while x == c[j+1]:
            j += 1
        #t5
        if j > t:
            print(counter)
            return
        #t6
        c[j-1] = x
        j -= 1

def algorithm_C(itr, t):
    counter = 0
    seq = list(itr)
    n = len(seq)
    s = n - t
    #c1
    a = [0 if i < s else 1 for i in range(n)]
    w = [1 for i in range(n)]
    r = s if s > 0 else t
    while True:
        #c2
        counter += 1
        yield [seq[i] for i, e in enumerate(a) if e == 1]
        j = r
        # this stupid while loop
        while j <= n-1:
            if w[j] == 0:
                w[j] = 1
                j += 1
            else:
                break
        if j == n:
            print(counter)
            return
        w[j] = 0
        #c4
        if j % 2 != 0 and a[j] != 0:
            a[j-1] = 1
            a[j] = 0
            if r == j > 1:
                r = j - 1
            elif r == j - 1:
                r = j
        #c5
        elif j % 2 == 0 and a[j] != 0:
            if a[j-2] != 0:
                a[j - 1] = 1
                a[j] = 0
                if r == j > 1:
                    r = j - 1
                elif r == j - 1:
                    r = j
            else:
                a[j-2] = 1
                a[j] = 0
                if r == j:
                    r = max(j-2, 1)
                elif r == j - 2:
                    r = j-1
        #c6
        elif j % 2 == 0 and a[j] == 0:
            a[j] = 1
            a[j-1] = 0
            if r == j > 1:
                r = j - 1
            elif r == j - 1:
                r = j
        #c7
        elif j % 2 != 0 and a[j] == 0:
            if a[j-1] != 0:
                a[j] = 1
                a[j - 1] = 0
                if r == j > 1:
                    r = j - 1
                elif r == j - 1:
                    r = j
            else:
                a[j] = 1
                a[j-2] = 0
                if r == j - 2:
                    r = j
                elif r == j - 1:
                    r = j - 2

def random_combination(itr, k):
    seq = list(itr)
    n = len(seq)
    a = [i for i in range(n)]
    m = 0
    if k == n:
        return seq
    if k <= n//2:
        s = list()
        while m < k:
            j = random.choice(a)
            if j not in s:
                s.append(j)
                m += 1
        return [seq[i] for i in sorted(s)]
    else:
        last = n - 1
        while m < n-k:
            a.remove(random.randint(0, last))
            last -= 1
            m += 1
        return [seq[i] for i in a]

if __name__ == "__main__":
    # algorithm_L([5,6,7,8,9,10], 5)
    # algorithm_T(range(6), 3)
    # algorithm_C([6,7,8,9,10,11], 3)
    print(random_combination([5,6,7,8,9,10], 6))