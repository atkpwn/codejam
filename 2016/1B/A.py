

def solve():
    freq = {}
    for c in input():
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    count = {}
    seq = [('0', 'ZERO',   'Z'),
           ('6', 'SIX',    'X'),
           ('2', 'TWO',    'W'),
           ('4', 'FOUR',   'U'),
           ('7', 'SEVEN',  'S'),
           ('5', 'FIVE',   'F'),
           ('8', 'EIGHT',  'G'),
           ('3', 'THREE',  'T'),
           ('1', 'ONE',    'O'),
           ('9', 'NINE',   'I')]
    for v, word, c in seq:
        if c in freq and freq.get(c) > 0:
            count[v] = freq[c]
            d = freq[c]
            for x in word:
                freq[x] -= d
    return ''.join(count.get(x, 0) * x for x in map(str, range(0, 10)))


def main():
    for t in range(int(input())):
        print('Case #{}: {}'.format(t + 1, solve()))


if __name__ == '__main__':
    main()
