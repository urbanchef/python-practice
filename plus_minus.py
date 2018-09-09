


def plus_minus(arr):
    negative_count = 0
    positive_count = 0
    zeros = 0

    for number in arr:
        if number < 0:
            negative_count += 1
        elif number > 0:
            positive_count += 1
        else:
            zeros += 1
    result = [positive_count, negative_count, zeros]
    for item in result:
        compute = round(item/len(arr), 6)
        print("{:.6f}".format(compute))



def main():
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    plus_minus(arr[:n])


if __name__ == '__main__':
    main()