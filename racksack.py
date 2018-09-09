def knapsack_fractions():
    num_of_items, racksack_size = [int(i) for i in input().split()]
    items = []
    for _ in range(num_of_items):
        items.append(tuple(int(i) for i in input().split()))

    items_sorted = sorted(items, key=lambda x: x[0] / x[1], reverse=True)

    max_price = 0

    for item in items_sorted:
        if item[0] == 0:
            continue
        elif item[1] <= racksack_size:
            racksack_size -= item[1]
            max_price += item[0]
        else:
            piece_size = racksack_size / item[1]
            piece_price = item[0] * piece_size
            max_price += piece_price
            break
    print("{:.3f}".format(max_price))


if __name__ == '__main__':
    knapsack_fractions()