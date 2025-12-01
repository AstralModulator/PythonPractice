def nonogram_sequence(*binary_array):
    list = []
    consecutive = 0
    for binary in binary_array:
        if binary == 1:
            consecutive += 1
        elif binary == 0 and consecutive != 0:
            list.append(consecutive)
            consecutive = 0
    if consecutive != 0:
        list.append(consecutive)
    return list

example1= [1,1,1,0,1,1,1,0]
print(nonogram_sequence(*example1))
example_1 = [1, 1, 1, 0, 1, 1]
example_2 = [1, 0, 1, 1, 1, 1]
example_3 = [1, 1, 1, 1, 1, 1]
example_4 = [1, 0, 1, 0, 1, 1]
example_5 = [0, 0, 0, 0, 0, 0]
print(nonogram_sequence(*example_1))