data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

def check_if_report_is_safe(ns, retries=1, is_decreasing=None):
    if len(ns) == 1:
        return True
    if is_decreasing is None:
        is_decreasing = ns[1] < ns[0]
    for i in range(1, len(ns)):
        diff = ns[i] - ns[i-1]
        if is_decreasing:
            diff *= -1
        if diff < 1 or diff > 3:
            if retries > 0:
                ns = ns[i-1:i] + ns[i+1:]
                return check_if_report_is_safe(ns, retries=retries-1, is_decreasing=is_decreasing)
            else:
                return False
    return True

result = 0

for line in data.split('\n'):
    ns = list(map(int, line.split(' ')))
    if check_if_report_is_safe(ns) or check_if_report_is_safe(ns[1:], 0):
        result += 1

print(result)
