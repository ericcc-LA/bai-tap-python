'''
bai7: tinh ti le va so sanh
'''


def calculate_ratio(d, key1, key2):

    value1 = d[key1]

    value2 = d[key2]

    if value2 == 0:
        return 0

    ratio = value1 / value2
    return ratio


if __name__ == "__main__":
    diem_so = {
        "ki_1": 8,
        "ki_2": 9,
        "ki_3": 10
    }

    result = calculate_ratio(diem_so, "ki_1", "ki_3")

    print(result)
