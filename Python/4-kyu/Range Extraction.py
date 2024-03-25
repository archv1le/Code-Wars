def solution(args):
    if not args:
        return ''

    ranges = []
    start = args[0]
    end = args[0]

    for num in args[1:]:
        if num == end + 1:
            end = num
        else:
            if end - start >= 2:
                ranges.append('{}-{}'.format(start, end))
            else:
                ranges.extend(str(n) for n in range(start, end + 1))
            start = end = num

    if end - start >= 2:
        ranges.append('{}-{}'.format(start, end))
    else:
        ranges.extend(str(n) for n in range(start, end + 1))

    return ','.join(ranges)
