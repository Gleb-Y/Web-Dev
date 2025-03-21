def front_times(s, n):
    front = s[:3]
    result = ""
    for _ in range(n):
        result += front
    return result