from p02_7c import dieroll

def dieroller(n):
	count = 0
	for i in range(0,n):
		if dieroll() % 3 == 0:
			count += 1
	result = count / n
	return result

if __name__ == "__main__":
	t = input("Input how many times to roll dice:")
	try:
		print(dieroller(int(t)))
	except:
		print("Error occured!")
			