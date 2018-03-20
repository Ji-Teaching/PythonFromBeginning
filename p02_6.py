def percentile(arr, k):
	sorted_arr = sorted(arr)
	l = len(sorted_arr)
	if l == 0:
		print("There are no numbers in the array!")
		return	
	p = k * (l - 1)
	if p == int(p):
		result = sorted_arr[int(p)]
	else:
		d = p - int(p)
		# 这里我没太看明白题干给的百分位数公式是怎么回事
		# 照一般的百分位数定义，[1,2,3]的第25百分位数结果应该是1.5
		# 用Excel的PERCENTILE函数得出的结果也是1.5，而不是1.25
		result = d * sorted_arr[int(p)] + (1 - d) * sorted_arr[int(p) + 1]
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
	flag = False
	while not flag:
		v  = input("Input the percentile number (between 0 and 1):")
		try:
			v = float(v)
		except:
			print("The data you input is not a number!")
			continue
		if v < 0 or v > 1:
			print("The number is not valid!")
			continue
		flag = True
	print(percentile(a, v))