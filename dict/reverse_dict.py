
def reverse_dict(d: dict) -> dict:
    result = {}
    for key, value in d.items():
        result[value] = key
    return result


if __name__ == "__main__ ":
    print(reverse_dict({"a": 1, "b": 2, "c": 3}))
