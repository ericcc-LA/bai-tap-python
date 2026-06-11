

def merge_dicts(*dicts: dict):

    result = {}

    for i in dicts:
        for key, value in i.items():
            result[key] = value

    return result


if __name__ == "__main__":

    print(merge_dicts({"a": 1}, {"b": 2}, {"a": 3, "c": 4}))
