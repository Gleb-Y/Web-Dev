def count_hi(s):
    count = 0
    for i in range(len(s) - 1):
        if s[i] == 'h' and s[i+1] == 'i':
            count += 1
    return count