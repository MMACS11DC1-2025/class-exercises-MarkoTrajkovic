def is_light(r, g, b):
    if (r + g + b)/3 > 128:
        return True
    else:
        return False
