'''
b2: tinh %
'''


def calculate_percentage(d):

    total = 0
    for value in d.values():
        total = total + value

    result = {}
    for key, value in d.items():
        percent = value / total * 100
        result[key] = percent

    return result


if __name__ == "__main__":

    print(calculate_percentage({"apple": 50, "banana": 30, "orange": 20}))
