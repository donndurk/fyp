def algorithm_P(n):
    a = ['(' if i%2==0 else ')' for i in range(2*n)]
    a.insert(0, ')')
    m = (2 * n) -1

    while True:
        # input("Next?")
        val = a[1:]
        return_sequence(val)
        a[m] = ')'
        if a[m-1] == ')':
            a[m-1] = '('
            m -= 1
        else:
            j = m - 1
            k = (2 * n) - 1
            while a[j] == '(':
                # print(f"j={j}, k={k}")
                a[j] = ')'
                a[k] = '('
                j -= 1
                k -= 2
            if j == 0:
                return
            else:
                a[j] = '('
                m = (2 * n) - 1

def algorithm_B(n):
    l = [0 for i in range(1, n+1)]
    r = [0 for i in range(1, n+1)]
    for k in range(n):
        l[k-1] = k + 1
    l[n-1] = 0
    r[n-1] = 0
    l.append(1)
    while True:
        return_sequence(l[:-1])
        return_sequence(r)
        print()
        j = 0
        while l[j] == 0:
            r[j] = 0
            l[j] = j + 1
            j += 1
            if j > n:
                return
        y = l[j]
        k = 0
        while r[y] > 0:
            k = y
            y = r[y]
        if k > 0:
            r[k] = 0
        else:
            l[j] = 0
        r[y] = r[j]
        r[j] = y

def return_sequence(seq):
    output = ''
    for i in seq:
        output += str(i)
    print(output)

if __name__=='__main__':
    algorithm_B(4)

