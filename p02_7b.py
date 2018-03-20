from p02_7a import coinflip

def coinflipper(n):
	count = 0
	for i in range(0,n):
		if coinflip() == True:
			count += 1
	result = count / n
	return result

if __name__ == "__main__":
	t = input("Input how many times to flip a coin:")
	try:
		print(coinflipper(int(t)))
	except:
		print("Error occured!")
			