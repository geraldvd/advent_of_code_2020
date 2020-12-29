import math

def traverse(matrix, down_step, right_step):
    step_right_count = 0
    tree_count = 0
    for step_down_count in range(0, len(matrix), down_step):
        if matrix[step_down_count][step_right_count] == '#':
            tree_count += 1
        step_right_count += right_step
        if step_right_count >= len(matrix[step_down_count]):
            step_right_count -= len(matrix[step_down_count])
    return tree_count

matrix = []
with open('input_day3.txt', 'r') as f:
    for r in f:
        matrix.append(r.strip())
print(f'Answer problem 1: {traverse(matrix, 1, 3)}')
print(f'Answer problem 2: {math.prod([traverse(matrix, i, j) for (i,j) in zip([1, 1, 1, 1, 2],[1, 3, 5, 7, 1])])}')