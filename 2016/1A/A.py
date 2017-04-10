def solve():
    s = input()
    res = ''
    for i in s:
        if i + res > res + i:
            res = i + res
        else:
            res = res + i
    return res


def main():
    for t in range(int(input())):
        print('Case #{}: {}'.format(t + 1, solve()))


if __name__ == '__main__':
    main()
