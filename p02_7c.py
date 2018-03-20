import random

def dieroll():
	result = random.randrange(1,7)
	return result
	
if __name__ == "__main__":
	t = input("Input how many times to roll dice:")
	try:
		for i in range(0,int(t)):
			print(dieroll())
	except:
		print("Error occured!")
