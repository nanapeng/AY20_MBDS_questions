import pandas as pd

input_file1 = "/Users/peng/Desktop/AY20_MBDS_questions/Question 7/Question 7.1/input_coordinates_7_1.txt"
input_file2 = "/Users/peng/Desktop/AY20_MBDS_questions/Question 7/Question 7.1/input_index_7_1.txt"

input_coordinates = pd.read_csv(input_file1, sep = '\t')
input_index = pd.read_csv(input_file2, sep = '\t')

X = input_coordinates[['x1', 'x2']]
I = input_index['index']
L1 = 50

output_index = L1*X.x2 + X.x1
output_index = pd.DataFrame(output_index, columns = ['index'])
output_index.to_csv("output_index_7_1.txt", index = False)

output_x1 = I % L1
output_x2 = I // L1
output_coor = pd.DataFrame()
output_coor['x1'] = output_x1
output_coor['x2'] = output_x2
output_coor.to_csv("output_coordinates_7_1.txt", index = False, sep = '\t')
