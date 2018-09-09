
def classic_racksack():
    num_of_items, racksack_size = [int(i) for i in input().split()]
    items = []
    for _ in range(num_of_items):
        items.append(tuple(int(i) for i in input().split()))

    items_sorted = sorted(items, key=lambda x: x[1])

    current_size = 0
    max_price = 0
    for item in items_sorted:
        if (current_size + item[1]) <= racksack_size:
            current_size += item[1]
            max_price += item[0]
        else:
            item_piece = [item[0], item[1]]
            while (current_size + item_piece[1]) > racksack_size:
                item_piece[0] /= 2
                item_piece[1] /= 2
            current_size += item_piece[1]
            max_price += item_piece[0]
    print("{:.3f}".format(max_price))


def continuous_racksack():
    num_of_items, racksack_size = [int(i) for i in input().split()]
    items = []
    for _ in range(num_of_items):
        items.append(tuple(int(i) for i in input().split()))

    items_sorted = sorted(items, key=lambda x: x[1])

    current_size = 0
    max_price = 0
    for item in items_sorted:
        if item[0] == 0:
            continue
        elif (current_size + item[1]) <= racksack_size:
            current_size += item[1]
            max_price += item[0]
        else:
            item_piece = [item[0], item[1]]
            item_piece[1] = (racksack_size - current_size) / item_piece[1]
            item_piece[0] *= item_piece[1]
            current_size += item_piece[1]
            max_price += item_piece[0]
    print("{:.3f}".format(max_price))



if __name__ == '__main__':
    # classic_racksack()
    continuous_racksack()