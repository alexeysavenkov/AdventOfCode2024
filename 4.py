data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".split("\n")

possible_offsets = [
    [(0,0), (0,1), (0,2), (0,3)],
    [(0,0), (1,1), (2,2), (3,3)],
    [(0,0), (1,0), (2,0), (3,0)],
    [(0,0), (1,-1), (2,-2), (3,-3)]
]

possible_words = ["XMAS", "SAMX"]

result = 0

def is_valid_point(y,x):
    if y < 0 or y >= len(data):
        return False
    if x < 0 or x >= len(data[y]):
        return False
    return True

def get_word(y0,x0,offset):
    res = ''
    for x1, y1 in offset:
        x = x0+x1
        y = y0+y1
        if is_valid_point(y,x):
            res += data[y][x]
    return res

for y in range(len(data)):
    for x in range(len(data[y])):
        for offset in possible_offsets:
            word = get_word(y,x,offset)
            print("WORD", word)
            if word in possible_words:
                result += 1

print(result)
