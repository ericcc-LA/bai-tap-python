'''
bai 10 caculate profit
'''


def caculate_profit(investments):

    result = {}

    for name, data in investments.items():

        invested = data["invested"]

        current = data["current"]

        profit = current - invested

        roi = profit / invested * 100

        roi = profit * 100 / invested

        result[name] = {
            "profit": profit,
            "roi": roi
        }

    return result


if __name__ == "__main__":

    investments = {
        "BTC": {"invested": 1000, "current": 1360},
        "ETH": {"invested": 500,  "current": 755},
        "SOL": {"invested": 200,  "current": 150},
    }
    result = caculate_profit(investments)

    print(result)

    print("-------")

    for name, info in result.items():
        print(f"{name}: profit = {info['profit']}, ROI = {info['roi']:.1f}%")
