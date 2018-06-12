#while 

count = 0

while count < 10 :

	print("while count=" + str(count))

	count = count + 1

# for

chars = "ABCDEFG"

for c in chars:

	print("for 1 :"+c)

#array

array = ["Hello ", "I ", "am ", "Python"]

for char in array :

	print("for 2 :"+char)

for chars in array :
	for c in chars :
		print("for 3 :"+c)

