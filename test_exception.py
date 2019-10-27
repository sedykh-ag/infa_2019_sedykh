c=0

try:
	a=1
	b=2
	#e = a / 0
	c = 2 + "a"
except ZeroDivisionError:
	print("division_by_zero")
	k = 0
except TypeError as b:
	print("TypeError")
	c=1
	print(c)


