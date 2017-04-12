def minimize(c, i):
    return c[i:].replace('?', '0')


def maximize(c, i):
    return c[i:].replace('?', '9')


def solve():
    def fill(cc, jj):
        if int(cc) > int(jj):
            return cc + minimize(c, i + 1), jj + maximize(j, i + 1)
        else:
            return cc + maximize(c, i + 1), jj + minimize(j, i + 1)

    c, j = input().split()
    cc, jj = '', ''
    feasible = []
    for i in range(len(c)):
        if c[i] == '?' and j[i] == '?':
            for x, y in [('1', '0'), ('0', '1')]:
                feasible.append(fill(cc + x, jj + y))
            cc += '0'
            jj += '0'
        elif c[i] == '?':
            if j[i] < '9':
                feasible.append(fill(cc + str(int(j[i]) + 1), jj + j[i]))
            if j[i] > '0':
                feasible.append(fill(cc + str(int(j[i]) - 1), jj + j[i]))
            cc += j[i]
            jj += j[i]
        elif j[i] == '?':
            if c[i] < '9':
                feasible.append(fill(cc + c[i], jj + str(int(c[i]) + 1)))
            if c[i] > '0':
                feasible.append(fill(cc + c[i], jj + str(int(c[i]) - 1)))
            cc += c[i]
            jj += c[i]
        else:
            if c[i] == j[i]:
                cc += c[i]
                jj += j[i]
            else:
                feasible.append(fill(cc + c[i], jj + j[i]))
                break
    if len(cc) == len(c):
        feasible.append((cc, jj))
    dif = 10**20
    res = None
    for x, y in map(lambda t: map(int, t), feasible):
        v = abs(x - y)
        if v < dif or \
           v == dif and x + y < sum(res) or \
           v == dif and x + y == sum(res) and y < res[1]:
            dif = v
            res = (x, y)
    return '{} {}'.format(*map(lambda s: s.zfill(len(c)),  map(str, res)))


def main():
    for t in range(int(input())):
        print('Case #{}: {}'.format(t + 1, solve()))


if __name__ == '__main__':
    main()
