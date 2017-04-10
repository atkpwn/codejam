def solve():
    n = int(input())
    count = {}
    res = []
    for i in range(2 * n - 1):
        for j in map(int, input().split()):
            count[j] = count.get(j, 0) + 1
    for k in count:
        if count[k] % 2 == 1:
            res.append(k)
    return ' '.join(map(str, sorted(res)))


def main():
    for t in range(int(input())):
        print('Case #{}: {}'.format(t + 1, solve()))


if __name__ == '__main__':
    main()
