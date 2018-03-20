def median(arr):
	sorted_arr = sorted(arr)
	l = len(sorted_arr)
	if l == 0:
		print("There are no numbers in the array!")
		return
	if l % 2 == 1:
		result = sorted_arr[int((l - 1) / 2)]
	else:
		result = (sorted_arr[int((l / 2) - 1)] + sorted_arr[int(l / 2)]) / 2
	return result
	
if __name__=="__main__":
	a = list()
	loop = True
	while loop:
		num = input("Input an array of numbers (type 'f' to finish):")
		if num == 'f':
			loop = False
			break
		else:
			try:
				num = float(num)
			except:
				print("The data you input is not a number!")
				continue
			a.append(num)
		if len(a) > 99:
			break
	print(median(a))