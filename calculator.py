def add(a,b):
	return a+b

def subtract(a,b):
	return a-b

def multiply(a,b):
	return a*b

def divide(a,b):
	return a/b

def square(a):
	return a*a

def cube(a):
	return a*a*a

def square_n_times(a,n):
	for n in range(n):
		a = a*a
	return a


print ("I'm going use the calculator functions to multiply 5 and 6")
x = multiply(5,6)
print(x)

print ("Test square n times, 2 squared 4 times")
y = square_n_times(2,4)
print(y)
