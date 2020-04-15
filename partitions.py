import random

# integer partitions

def algorithm_P(n):
    # p1
    a = [0 for i in range(n + 1)]
    m = 1
    while True:
        # p2
        a[m] = n
        if n == 1:
            q = m - n
        else:
            q = m

        while True:
            # p3
            return_sequence(a[1:m+1])
            # print(a, "q =", q, "- m =", m, "- n =", n)
            if a[q] != 2:
                #p5
                if q == 0:
                    return
                x = a[q] - 1
                a[q] = x
                n = m - q + 1
                m = q + 1

                #p6
                while True:
                    if n <= x:
                        go_to_p2 = True
                        break
                    else:
                        a[m] = x
                        m += 1
                        n -= x
                if go_to_p2:
                    go_to_p2 = False
                    break
            else:
                # p4
                a[q] = 1
                q -= 1
                m += 1
                a[m] = 1

def algorithm_H(n, m):
    if n < 2 or m < 2 or m > n:
        return
    #h1
    a = [1 for i in range(m+1)]
    a[0] = n - m + 1
    a[m] = -1

    while True:
        #h2
        return_sequence(a[:m])
        if a[1] >= a[0] - 1:
            #h4
            j = 2
            s = a[0] + a[1] - 1
            while a[j] >= a[0] - 1:
                s += a[j]
                j += 1
            #h5
            if j >= m:
                return
            x = a[j] + 1
            a[j] = x
            j -= 1
            #h6
            while j > 0:
                a[j] = x
                s -= x
                j -= 1
            a[0] = s
        else:
            #h3
            a[0] -= 1
            a[1] += 1

# ----------------------------------------------------------------------------------
# set partitions

def algorithm_H_set(n):
    if n < 2:
        return
    #h1
    a = [0 for i in range(n)]
    b = [1 for j in range(n-1)]
    m = 1
    while True:
        #h2
        return_sequence(a)
        if a[n-1] == m:
            #h4
            j = n - 2
            while a[j] == b[j]:
                j -= 1
            #h5
            if j == 0:
                return
            a[j] += 1
            #h6
            k = 1 if a[j] == b[j] else 0
            m = b[j] + k
            j += 1
            while j < n - 1:
                a[j] = 0
                b[j] = m
                j += 1
            a[n-1] = 0
        else:
            #h3
            a[n-1] += 1

def random_partition(n):
    return [random.randint(0, n-1) for i in range(n)]

def return_sequence(seq):
    print(''.join(str(x) for x in seq))
    return seq

if __name__ == '__main__':
    # algorithm_P(25)
    # algorithm_H(4, 5)
    # algorithm_H_set(4)
    print(random_partition(4))