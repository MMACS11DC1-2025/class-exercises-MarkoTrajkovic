def is_flag(r, g, b):
    if r >= 240 and g >= 240 and b >= 240:
        return "white"
    elif r >= 240 and g < 25 and b < 25:
        return "red"
    elif r < 25 and g < 25 and b > 240:
        return "blue"
    else:
        return "other"