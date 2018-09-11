def time_conversion(time_string):
    daytime = time_string[-2:]
    hours, minutes, seconds = [int(i) for i in time_string[:-2].split(':')]
    if daytime == 'AM' and hours == 12:
        hours = 0
    elif daytime =='PM' and hours == 12:
        hours = 12
    elif daytime == 'PM' and 1 <= hours <= 11:
        hours += 12
    print("{:0>2}:{:0>2}:{:0>2}".format(hours, minutes, seconds))


if __name__ == '__main__':
    time_string = '08:02:00AM'
    time_conversion(time_string)