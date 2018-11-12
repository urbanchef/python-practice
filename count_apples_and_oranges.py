def count_apples_and_oranges(s, t, a, b, apples, oranges):
    apples_in_range = []
    oranges_in_range = []
    for apple in apples:
        if s <= a + apple <= t:
            apples_in_range.append(apple)
    for orange in oranges:
        if s <= b + orange <= t:
            oranges_in_range.append(orange)
    print(len(apples_in_range))
    print(len(oranges_in_range))


