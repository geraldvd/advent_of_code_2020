def parse_passports(raw_passport_input):
    passports_raw = raw_passport_input.split('\n\n')
    passports = [p.replace('\n', ' ').split(' ') for p in passports_raw]
    passports = [[tuple(field.split(':')) for field in p] for p in passports]
    passports = [[f for f in p if len(f)==2] for p in passports]
    return passports

def validate_passport_problem1(passport):
    keys_required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    if not (7 <= len(passport) <= 8):
        return False   
    keys = [f[0] for f in p]
    for k in keys_required:
        if k not in keys:
            return False
    return True

def validate_passport_problem2(passport):
    if not validate_passport_problem1(passport):
        return False  
    for f in passport:
        k = f[0]
        v = f[1]
        if k == 'byr':
            if not 1920 <= int(v) <= 2002:
                return False
        elif k == 'iyr':
            if not 2010 <= int(v) <= 2020:
                return False
        elif k == 'eyr':
            if not 2020 <= int(v) <= 2030:
                return False
        elif k == 'hgt':
            if len(v) < 3:
                return False
            if v[-2:] == 'in':
                v = int(v.rstrip('in'))
                if not 59 <= int(v) <= 76:
                    return False
            elif v[-2:] == 'cm':
                v = int(v.rstrip('cm'))
                if not 150 <= int(v) <= 193:
                    return False
            else:
                return False
        elif k == 'hcl':
            if len(v) != 7 or v[0] != '#' or not v[1:].isalnum():
                return False
        elif k == 'ecl':
            if v not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return False
        elif k == 'pid':
            if len(v) != 9 or not v.isnumeric():
                return False
    return True


with open('input_day4.txt', 'r') as f:
    passports = parse_passports(f.read())
    valid_passports_problem1 = 0
    valid_passports_problem2 = 0
    for p in passports:
        if validate_passport_problem1(p):
            valid_passports_problem1 += 1
        if validate_passport_problem2(p):
            valid_passports_problem2 += 1
    print(f'Answer problem 1: {valid_passports_problem1}')
    print(f'Answer problem 2: {valid_passports_problem2}')