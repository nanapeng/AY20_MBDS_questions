"""
To find operations needed to get the desired sum
with the given m*n matrix composed of regular numbers, the sum of each column is the same
we need to choose from rows to get the remaining sum, except the value of point(1,1) and point(m,n)
then, arrange the chosen numbers in ascending order to get operations
"""


def solution(m, n, desired_sum):
    col_sum = 0
    num = []
    for i in range(1, m + 1):
        col_sum = col_sum + i
        num.append(i)  # put the consecutive numbers that must be selected in the column into num

    row_sum = desired_sum - col_sum
    row_num = n - 1  # number of values need to be selected to meet row sum

    # take special values according to restrictios(row sum and number of values)
    num1 = row_sum // row_num
    num2 = num1 + row_sum % row_num

    # put numbers in num, and arrange chosen numbers in ascending order
    for i in range(n - 2):
        num.append(num1)

    num.append(num2)
    num.sort()

    # associate numerical changes with right and down operations, operations is one less than values
    for i in range(len(num) - 1):
        if num[i] == num[i + 1]:
            num[i] = "R"
        else:
            num[i] = "D"

    num.pop()  # delete last value
    num = "".join(num)
    return num


with open('output_question_1', 'a') as f:
    m = (9, 9, 9, 9, 90000, 90000)
    n = (9, 9, 9, 9, 100000, 100000)
    desired_sum = (65, 72, 90, 110, 87127231192, 5994891682)
    for i in range(len(m)):
        f.write("%s %s\n" % (desired_sum[i], solution(m[i], n[i], desired_sum[i])))