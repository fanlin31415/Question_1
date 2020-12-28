def operations(m, n, num):

	sum_of_col_axis = (1 + m) * m // 2

	rest_sum = num - sum_of_col_axis

	if (rest_sum > m*(n-1)):
		return "NO OPERATIONS"

	average = rest_sum // (n-1)

	remainder_num = rest_sum - average * (n-1)

	average_num = (n-1) - remainder_num


	l = [0 for i in range(m)]
	l[average-1] += average_num
	l[average] += remainder_num


	res = ""
	for num_occurence in l:
		if num_occurence == 0:
			res += "D"
		else:
			res += "D" + "R"*num_occurence

	return res[1:]


# example
print('summed number is 13', operations(4,4,13))
print('summed number is 16', operations(4,4,16))
print('summed number is 19', operations(4,4,19))
print('\n')

# question 1.a
print('summed number is 65', operations(9,9,65))
print('summed number is 72', operations(9,9,72))
print('summed number is 90', operations(9,9,90))
print('summed number is 110', operations(9,9,110))
print('\n')

# question 1.b
print('summed number is 87127231192', operations(90000,100000,87127231192))
print('summed number is 5994891682', operations(90000,100000,5994891682))

