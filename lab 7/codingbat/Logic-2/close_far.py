def close_far(a, b, c):
    def is_close(x, y):
        return abs(x - y) <= 1
    def is_far(x, y, z):
        return abs(x - y) >= 2 and abs(x - z) >= 2
    if is_close(a, b) and is_far(a, c, b):
        return True
    if is_close(a, c) and is_far(a, b, c):
        return True
    return False