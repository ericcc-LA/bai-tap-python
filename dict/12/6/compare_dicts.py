'''
bai 4 : so sanh dict va tinh chenh leechj

'''

def compare_dicts(before, after):
    result = {}

    for key in before:
        old_value = before[key]
        new_value = after[key]

        change = new_value - old_value
        percent_change = (change / old_value) * 100

        result[key] = {
            "old": old_value,
            "new": new_value,
            "change": change,
            "percent_change": percent_change
        }

    return result


if __name__ == "__main__":

    before = {"product1": 100, "product2": 50}
    after = {"product1": 120, "product2": 40}

    output = compare_dicts(before, after)
    print(output)
