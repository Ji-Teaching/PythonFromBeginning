import random

def coinflip():
	s = random.random()
	if float(s) < 0.5:
		return True
	else:
		return False
		
if __name__ == "__main__":
	t = input("Input how many times to flip a coin:")
	try:
		for i in range(0,int(t)):
			print(coinflip())
	except:
		print("Error occured!")
