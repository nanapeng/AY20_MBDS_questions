import pandas as pd

input_file1 = "/Users/peng/Desktop/AY20_MBDS_questions/Question 7/Question 7.2/input_coordinates_7_2.txt"
input_file2 = "/Users/peng/Desktop/AY20_MBDS_questions/Question 7/Question 7.2/input_index_7_2.txt"

input_coordinates = pd.read_csv(input_file1, sep = '\t')
input_index = pd.read_csv(input_file2, sep = '\t')

X = input_coordinates[['x1', 'x2', 'x3', 'x4', 'x5', 'x6']]
I = input_index['index']
(L1, L2, L3, L4, L5, L6) = (4, 8, 5, 9, 6, 7)

output_index = X.x1 + L1*X.x2 + L1*L2*X.x3 + L1*L2*L3*X.x4 + L1*L2*L3*L4*X.x5 + L1*L2*L3*L4*L5*X.x6
output_index = pd.DataFrame(output_index, columns = ['index'])
output_index.to_csv("output_index_7_2.txt", index = False)

output_x1 = I % (L1*L2*L3*L4*L5) % (L1*L2*L3*L4) % (L1*L2*L3) % (L1*L2) % L1
output_x2 = (I % (L1*L2*L3*L4*L5) % (L1*L2*L3*L4) % (L1*L2*L3) % (L1*L2)) // L1
output_x3 = (I % (L1*L2*L3*L4*L5) % (L1*L2*L3*L4) % (L1*L2*L3)) // (L1*L2)
output_x4 = (I % (L1*L2*L3*L4*L5) % (L1*L2*L3*L4)) // (L1*L2*L3)
output_x5 = (I % (L1*L2*L3*L4*L5)) // (L1*L2*L3*L4)
output_x6 = I // (L1*L2*L3*L4*L5)

output_coor = pd.DataFrame()
output_coor['x1'] = output_x1
output_coor['x2'] = output_x2
output_coor['x3'] = output_x3
output_coor['x4'] = output_x4
output_coor['x5'] = output_x5
output_coor['x6'] = output_x6

output_coor.to_csv("output_coordinates_7_2.txt", index = False, sep = '\t')