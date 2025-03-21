def make_chocolate(small, big, goal):
    max_big = goal // 5
    if big > max_big:
        big = max_big
    remaining = goal - (big * 5)
    if remaining <= small:
        return remaining
    return -1