def make_bricks(small, big, goal):
    max_big = goal // 5
    if big > max_big:
        big = max_big
    return goal - (big * 5) <= small