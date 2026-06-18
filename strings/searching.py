'''
bai 3
'''


def find_all_indices(s, substring):

    result = []
    i = 0

    while i <= len(s) - len(substring):
        if s[i:i+len(substring)] == substring:

            result.append(i)

        i += 1
    return result


def count_word_frequency(text):

    text = text.lower()
    for p in str.punctuation:
        text = text.replace(p, "")

    words = text.split()

    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq


def find_longest_word(text):

    words = text.split()
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


if __name__ == "__main__":
    print(find_all_indices("aabaab", "aa"))
    print(count_word_frequency("hello world hello python"))
    print(find_longest_word("The quick brown fox jumps"))
