def policy_problem1(x):
    rule, password = x.split(':')
    num_occurances, character = rule.split(' ')
    password = password.strip()
    num_chars_in_pass = password.count(character.strip())
    min_count, max_count = num_occurances.strip().split('-')
    return int(num_chars_in_pass) in range(int(min_count), int(max_count)+1)

def policy_problem2(x):
    rule, password = x.split(':')
    positions, character = rule.split(' ')
    password = password.strip()
    pos1, pos2 = positions.strip().split('-')
    return bool(password[int(pos1)-1]==character) != bool(password[int(pos2)-1]==character)

problem1_count = 0
problem2_count = 0
with open('input_day2.txt', 'r') as f:
    for r in f:
        if policy_problem1(r):
            problem1_count += 1
        if policy_problem2(r):
            problem2_count += 1
print(f'Answer problem 1: {problem1_count}')
print(f'Answer problem 2: {problem2_count}')