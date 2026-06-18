'''
bai 5
'''


def pad_string(s, width, align="left", fill_char=" "):
    so_ky_tu_thieu = width - len(s)
    if so_ky_tu_thieu <= 0:
        return s
    if align == "left":
        return fill_char * so_ky_tu_thieu

    elif align == "center":

        trai = so_ky_tu_thieu // 2
        phai = so_ky_tu_thieu - trai
        return fill_char * trai + s + fill_char * phai

    else:
        return s

    print(pad_string("hi", 10, "left", "."))
    print(pad_string("hi", 10, "right", "."))
    print(pad_string("hi", 10, "center", "."))


def format_table(rows, col_widths):
    ket_qua = []
    for row in rows:
        cac_cot_da_pad = []

        for i in range(len(row)):
            gia_tri = str(row[i])
            do_rong = col_widths[i]

            cot_da_pad = pad_string(gia_tri, do_rong, "left")
            cac_cot_da_pad.append(cot_da_pad)
        dong_moi = " | ".join(cac_cot_da_pad)
        ket_qua.append(dong_moi)

    return "\n".join(ket_qua)


data = [
    ["Quan", "20", "Python"],
    ["An", "22", "Odoo"]
]
print(format_table(data, [6, 4, 8]))


def indent_text(text, spaces=4):
    khoang_trang = " " * spaces

    cac_dong = text.split("\n")

    cac_dong_moi = []
    for dong in cac_dong:
        dong_moi = khoang_trang + dong
        cac_dong_moi.append(dong_moi)

    return "\n".join(cac_dong_moi)


text = "Hello\nWorld\nPython"
print(indent_text(text, 4))
