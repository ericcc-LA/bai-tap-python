

def dict_difference(d1: dict, d2: dict) -> bool:

    result = {}

    for key in d1:

        if key not in d2:

            result[key] = (d1[key], None)

        elif d1[key] != d2[key]:

            result[key] = (d1[key], d2[key])

    for key in d2:

        if key not in d1:

            result[key] = (None, d2[key])

    return result

# def v2(d1: dict, d2: dict) -> bool:


if __name__ == "__main__":

    print(dict_difference({"a": 1, "b": 2}, {"a": 1, "b": 3}))
