def tick(length, label=" "):
    line = "-" * length
    if label:
        line += " " + label
    print(line)                                                    # 221910307033 (Likith Narukurthi)


def draw_interval(cen_len):
    if cen_len > 0:
        draw_interval(cen_len - 1)
        tick(cen_len)
        draw_interval(cen_len - 1)


def ruler(inches, major_len):                                       # 221910307033 (Likith Narukurthi)
    tick(major_len, "0")

    for i in range(1, inches + 1):
        draw_interval(major_len - 1)
        tick(major_len, str(i))


ruler(1, 5)