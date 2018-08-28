def is_between(l, r, c):
    return l <= c <= r


def find_points(segments):
    points = []
    sorted_segments = sorted(segments, key=lambda x: x[1])
    point = sorted_segments[0][1]
    points.append(point)
    for segment in sorted_segments[1:]:
        l, r = segment[0], segment[1]
        if is_between(l, r, point):
            continue
        else:
            point = r
            points.append(point)
    return len(points), points


if __name__ == '__main__':

    num_of_segments = int(input())
    segments = []
    for n in range(num_of_segments):
        segments.append(tuple([int(i) for i in input().split()]))

    num_of_points, points = find_points(segments)
    print(num_of_points)
    print(*points, sep=' ')









