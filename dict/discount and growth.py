'''
bai 3: tang , giam lai xuat
'''


def apply_growth(d, growth_rate):
    result = {}

    for key, value in d.items():
        tang_them = value * growth_rate / 100
        gia_moi = value + tang_them
        result[key] = gia_moi

    return result


def apply_discount(d, discount_rate):
    result = {}

    for key, value in d.items():
        giam_di = value * discount_rate / 100
        gia_moi = value - giam_di
        result[key] = gia_moi

    return result


if __name__ == "__main__":

    print(apply_growth({"product1": 100, "product2": 200}, 10))
    print(apply_discount({"apple": 50, "banana": 30}, 20))
