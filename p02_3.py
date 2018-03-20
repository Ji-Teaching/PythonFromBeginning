def mean(arr):
	sum = 0
	l = len(arr)
	if l == 0:
		print("There are no numbers in the array!")
		return
	for i in range(0,l):
		sum += arr[i]
	result = float(sum) / float(l)
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
	print(mean(a))
	