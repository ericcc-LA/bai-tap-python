'''
bai9 : tinh GPA
'''


def caculate_weaighted_average(d):

    total_score = 0

    total_credit = 0

    for _, info in d.items():

        score = info["score"]
        credit = info["credit"]

        total_score += score * credit

        total_credit += credit

    return total_score / total_credit


if __name__ == "__main__":

    scores = {
        "toan": {"score": 9.0, "credit": 4},
        "van": {"score": 7.0, "credit": 3},
        "anh": {"score": 8.0, "credit": 2}
    }

    result = caculate_weaighted_average(scores)

    print(result)
