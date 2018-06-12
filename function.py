var_a = 145
var_b = 13

def sumNumbers(a,b) :
	return a + b


def multiNumbers(a,b) :
	return a * b


def complex(a,b) :
	com_a = sumNumbers(a,b)
	com_b = multiNumbers(a,b)

	if com_a > com_b :
		return com_a
	else : 
		return com_b

#result

print(sumNumbers(var_a, var_b)) # result = 158
print(multiNumbers(var_a, var_b)) # result = 1885

print(complex(5,7)) #result = 35
print(complex(5, -7)) #result = -2


