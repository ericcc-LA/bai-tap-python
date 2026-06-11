

def filter_dict(d, predicate):

    result = {}

    for k, v in d.items():

        if predicate(k, v):

            result[k] = v

    return result


if __name__ == "__main__":
    data = []
    print(filter_dict(data, lambda k, v: v > 2))
