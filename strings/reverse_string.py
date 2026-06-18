'''
bai 1 : dao ngược string
'''


def reverse_string(s):
    result = ""

    for i in s:

        result = i + result
    return result


def get_char_at_indices(s, indices):

    result = ""

    for i in indices:

        result =result + s[i]

    return result


def extract_middle(s):

    n = len(s)

    mid = n // 2

    if n % 2 == 0:

        return s[mid - 1:mid + 1]

    else:
        return s[mid]


if __name__ == "__main__":

    print(reverse_string("hello"))
    print(get_char_at_indices("abcde", [0, 2, 4]))
    print(extract_middle("hello"))
    print(extract_middle("test"))
