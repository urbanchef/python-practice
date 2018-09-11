def birthday_cake_candles(candles):
    highest_candle_counter = 0
    the_highest = 0
    for candle in candles:
        if candle > the_highest:
            the_highest = candle

    for candle in candles:
        if candle == the_highest:
            highest_candle_counter += 1

    print(highest_candle_counter)


if __name__ == '__main__':
    candles = [int(i) for i in input().split()]
    birthday_cake_candles(candles)