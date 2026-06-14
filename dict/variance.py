'''
baif 6: thong ke co ban
'''


def calculate_variance(d):

    values = []
    for v in d.values():
        values.append(v)

    total = 0
    for num in values:
        total = total + num

    avg = total / len(values)

    sum_of_squares = 0
    for num in values:
        diff = num - avg
        diff_squared = diff ** 2
        sum_of_squares = sum_of_squares + diff_squared

    variance = sum_of_squares / len(values)

    return variance


def calculate_std_dev(d):

    variance = calculate_variance(d)

    std_dev = variance ** 0.5

    return std_dev


if __name__ == "__main__":
    data = {"a": 10, "b": 20, "c": 30}

    print(calculate_variance(data))
    print(calculate_std_dev(data))
