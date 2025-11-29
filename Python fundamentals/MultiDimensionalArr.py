import numpy as np

my_array = np.array([
    [['A','B','C'],['D','E','F'],['G','H','I']],
    [['J','K','L'],['M','N','O'],['P','Q','R']],
    [['S','T','U'],['V','W','X'],['Y','Z',' ']]])
print(my_array.ndim)
word = my_array[0,0,0] + my_array[2,0,0] + my_array[2,0,0]
print(word)

