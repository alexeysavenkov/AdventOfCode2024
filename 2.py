data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

def check_if_report_is_safe(line):
    ns = list(map(int, line.split(' ')))
    is_decreasing = ns[1] < ns[0]
    for i in range(1, len(ns)):
        diff = ns[i] - ns[i-1]
        if is_decreasing:
            diff *= -1
        if diff < 1 or diff > 3:
            return False
    return True

result = 0

for line in data.split('\n'):
    if check_if_report_is_safe(line):
        result += 1

print(result)
