def various_terms(n):
    terms = []
    current_num = 0
    remainder = n
    while True:
        current_num += 1
        if current_num * 2 < remainder:
            terms.append(current_num)
            remainder -= current_num
        else:
            terms.append(remainder)
            break
    print(len(terms))
    print(*terms, sep=' ')


if __name__ == '__main__':
    n = int(input())
    various_terms(n)