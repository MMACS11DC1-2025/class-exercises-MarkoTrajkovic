def is_flag(r, g, b):
    if 200 <= r <= 255 and 200 <= g <= 255 and 200 <= b <= 255:
        return "white"
    elif 100 <= r <= 255 and 0 <= g <= 120 and 0 <= b <= 120:
        return "red"
    elif 0 <= r <= 100 and 0 <= g <= 100 and 0 <= b <= 255:
        return "blue"
    else:
        return "other"