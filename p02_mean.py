def mean(num_list):
	sum = 0
	input_len = len(num_list)
	try:
		for i in range(input_len):
			sum += num_list[i]
	except:
		raise TypeError("Invalid data type!")
	try:
		return float(sum) / input_len
	except:
		raise ZeroDivisionError("List is empty!")
