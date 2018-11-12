def minimum_absolute_difference(arr):
    i = 0
    arr.sort()
    min_difference = abs(arr[0] - arr[1])
    while i < len(arr) - 1:
        difference = abs(arr[i] - arr[i + 1])
        if difference < min_difference:
            min_difference = difference
        i += 1
    return min_difference


if __name__ == '__main__':
    arr = [-2, 2, 4]
    result = minimum_absolute_difference(arr)
    print(result)

