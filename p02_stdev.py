from p02_mean import mean

def stdev(num_list):
	sum = 0
	input_len = len(num_list)
	if input_len == 0:
		raise ZeroDivisionError("List is empty!")
	mean_num = mean(num_list)
	for i in range(input_len):
		sum += (num_list[i] - mean_num) ** 2
	try:
		return (float(sum) / float(input_len - 1)) ** 0.5
	except:
		raise ZeroDivisionError("List contains only one number!")
