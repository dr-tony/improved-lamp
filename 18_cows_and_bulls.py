#gnerates a random number, then you have to guess what it is
def ranum_guess():
	"""random number to guess nad plays twice"""
	import random
	x = random.randrange(0, 9999)
	y = str(x)
	#print(y)
	count = 0
	active = True
	while active:

		a = input("Enter number a 4 digit number: ")
		num = str(a)
		print(num)
		y != num
		while True:
			y != num
			if num[0] == y[0]:
				print(num[0] + " = " + y[0] + " at pos 1") 
			if num[1] == y[1]:
				print(num[1] + " = " + y[1] + " at pos 2") 
			if num[2] == y[2]:
				print(num[2] + " = " + y[2] + " at pos 3") 
			if num[3] == y[3]:
				print(num[3] + " = " + y[3] + " at pos 4") 
			count += 1
			break
		if y == num:
		
			print("Well Done!! End of Game !!")
			print(str(count) + " attempts")
			active = False
ranum_guess()
print("Another game .....")
ranum_guess()

