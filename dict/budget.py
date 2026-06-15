'''
bài5: tính ngân sách
'''


def allocate_budget(total_budget, percentages):

    result = {}

    for key in percentages:
        percent = percentages[key]
        amount = total_budget * percent / 100
        result[key] = amount

    return result


def validate_budget(d):

    total = 0

    for key in d:
        total = total + d[key]

    if total == 100:
        return True
    else:
        return False


if __name__ == "__main__":

    percentages = {"marketing": 30, "engineering": 50, "operations": 20}

    kiem_tra = validate_budget(percentages)
    print(kiem_tra)
