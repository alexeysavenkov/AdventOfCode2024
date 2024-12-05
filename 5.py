rules = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13"""

updates = """75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

rule_dict = {}

for rule in rules.split("\n"):
    a, b = rule.split("|")
    if a not in rule_dict:
        rule_dict[a] = []
    rule_dict[a].append(b)

#print(rule_dict)

def is_update_in_the_right_order(pages):
    for i in range(0, len(pages)):
        for j in range(i+1, len(pages)):
            p1, p2 = pages[i], pages[j]

            rules_are_followed = p1 not in rule_dict.get(p2, {})

            if not rules_are_followed:
                #print(rule, p1, p2)
                return False
    return True

def get_middle_number(pages):
    return pages[len(pages)//2]

result = 0

for update in updates.split("\n"):
    pages = update.split(",")

    if is_update_in_the_right_order(pages):
        result += int(get_middle_number(pages))

print(result)
        
