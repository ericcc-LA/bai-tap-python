'''
bai 4 strings ralace & trànormation

'''


def replace_all(s, old, new):

    parts = s.split(old)
    return new.join(parts)


def swap_case(s):

    result = ""
    for ch in s:
        if ch.isupper():
            result += ch.lower()
        elif ch.islower():
            result += ch.upper()
        else:
            result += ch
    return result


def capitalize_words(s):

    words = s.split(" ")
    result = []
    for word in words:
        if word:
            new_word = word[0].upper() + word[1:].lower()
            result.append(new_word)
        else:
            result.append(word)
    return " ".join(result)


if __name__ == "__main__":
    print(replace_all("hello world hello", "hello", "hi"))
    print(swap_case("HeLLo WoRLd"))
    print(capitalize_words("hello world python"))
