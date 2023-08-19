def read_ints():
    with open('random_nums.txt', 'r') as f:
        data = f.read()
        nums = [int(x) for x in data if x.isdigit()]
        return nums


def count():
    nums = read_ints()
    return len(nums)


def summation():
    nums = read_ints()
    return sum(nums)


def average():
    return summation()/count()


def minimum():
    return min(read_ints())


def maximum():
    return max(read_ints())
