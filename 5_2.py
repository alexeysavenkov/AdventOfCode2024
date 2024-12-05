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
rule_dict_reverse = {}

for rule in rules.split("\n"):
    a, b = rule.split("|")
    if a not in rule_dict:
        rule_dict[a] = set()
    rule_dict[a].add(b)
    if b not in rule_dict_reverse:
        rule_dict_reverse[b] = set()
    rule_dict_reverse[b].add(a)

def get_rule_dict_reverse_copy(pages):
    res = {}
    for k,v in rule_dict_reverse.items():
        res[k] = set()
        for elem in v:
            if elem in pages:
                res[k].add(elem)
    return res
    

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

def fix_order(pages):
    new_order = []
    rule_dict_reverse_copy = get_rule_dict_reverse_copy(pages)

    while len(pages) > 0:
        next_elem = None
        for p in pages:
            if len(rule_dict_reverse_copy.get(p, [])) == 0:
                next_elem = p
                break

        print(pages)
        
        assert next_elem is not None
        new_order.append(next_elem)
        pages.remove(next_elem)
        for k, v in rule_dict_reverse_copy.items():
            if next_elem in v:
                v.remove(next_elem)

    return new_order
    

def get_middle_number(pages):
    return pages[len(pages)//2]

result = 0

for update in updates.split("\n"):
    pages = update.split(",")

    if is_update_in_the_right_order(pages):
        #result += int(get_middle_number(pages))
        pass
    else:
        fixed_order = fix_order(pages)
        result += int(get_middle_number(fixed_order))

print(result)
        
