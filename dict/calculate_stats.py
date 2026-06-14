'''
b1: tinhs tong , trung binh , min, max
'''


def calculate_stats(d):
    values = list(d.values())

    total = 0
    for num in values:
        total = total + num

    avg = total / len(values)

    min_val = values[0]
    max_val = values[0]

    for num in values:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    return {
        "sum": total,
        "avg": avg,
        "min": min_val,
        "max": max_val
    }


if __name__ == "__main__":

    print(calculate_stats({"a": 10, "b": 20, "c": 30, "d": 40}))
