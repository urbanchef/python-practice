
def mini_max_sum(arr):
    arr_sorted = sorted(arr)
    print(sum(arr_sorted[:4]), sum(arr_sorted[-4:]), sep=' ')


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    mini_max_sum(arr)