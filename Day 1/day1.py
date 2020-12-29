import math

# Problem 1
f = open('input_day1.txt', mode='r')
input_numbers = [int(i) for i in f]
diff_numbers = [2020-i for i in input_numbers]
intersection = list(set(input_numbers) & set(diff_numbers))
print(f'Answer problem 1: {intersection[0]*intersection[1]}')

# Problem 2
def problem2(input_numbers):
    for n1 in input_numbers:
        for n2 in input_numbers:
            for n3 in input_numbers:
                if n1+n2+n3 == 2020:
                    return n1*n2*n3
                    
print(f'Answer problem 2: {problem2(input_numbers)}')
