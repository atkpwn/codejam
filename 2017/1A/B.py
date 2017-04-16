from math import ceil, floor


def select(q, start):
    for j in range(start[0], len(q[0])):
        l, u = q[0][j]
        if l <= u:
            start[0] = j
            lower = l
            upper = u
            progress = True
            i = 1
            while i < len(q) and progress:
                progress = False
                for j in range(start[i], len(q[0])):
                    l, u = q[i][j]
                    if lower <= u and l <= upper:
                        start[i] = j
                        lower = max(lower, l)
                        upper = min(upper, u)
                        progress = True
                        i += 1
                        break
            if progress:
                return True
    return False


def solve():
    n, p = map(int, input().split())

    r = list(map(int, input().split()))
    q = [sorted(map(int, input().split())) for i in range(n)]
    for i in range(n):
        for j in range(p):
            upper = floor(q[i][j] / r[i] / 0.9)
            lower = ceil(q[i][j] / r[i] / 1.1)
            q[i][j] = (lower, upper)
    res = 0
    start = [0] * n
    while select(q, start):
        start = [s + 1 for s in start]
        res += 1
    return res


def main():
    for t in range(int(input())):
        print('Case #{}: {}'.format(t + 1, solve()))


if __name__ == '__main__':
    main()
