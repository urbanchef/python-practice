def diagonal_difference(arr):
    i = 0
    j = len(arr)
    prim_diag_sum = 0
    sec_diag_sum = 0
    while i < len(arr) and j > 0:
        sec_diag_sum += arr[i][j - 1]
        prim_diag_sum += arr[i][i]
        i += 1
        j -= 1
    return abs(prim_diag_sum - sec_diag_sum)


def main():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonal_difference(arr)
    print(result)


if __name__ == '__main__':
    main()