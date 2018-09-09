def staircase(n):
    i = n - 1
    j = 1
    for _ in range(n):
        print(' ' * i, '#' * j, sep='')
        i -= 1
        j += 1



if __name__ == '__main__':
    staircase(6)