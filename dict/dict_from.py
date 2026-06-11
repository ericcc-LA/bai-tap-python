
# input example: [ (2, 3), (4, 5), (6, 7) ]
def dic_from_pairs(pairs: list[tuple]):

    result = {}

    # for item in pairs ----- key = item[0], value = item[1]
    for key, value in pairs:

        result[key] = value

    return result


def getKey(num: int) -> str:
    return f'num_{num}'


def getValue(num: int) -> int:
    return num ** 2

# [1, 2, 3] -> key `num_1`, 'num_2`


def dict_from_list(inputs: list[int], func1, func2) -> dict:
    result = {}
    for num in inputs:
        key = func1(num)
        value = func2(num)
        result[key] = value
    
    return result


if __name__ == "__main__":
    inputs = [1, 2, 3, 4]
    result = dict_from_list(inputs, getKey, getValue)
    print(result)
