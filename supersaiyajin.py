def increaseKi(numbers):
	original=[]
	for i in range(len(numbers)):
		original.append(numbers[i])
	
	for i in range(len(numbers)):
		suma=0
		for x in range(len(numbers)):
			if x!=i:suma+=original[x]
		suma%=1000000007
		numbers[i]=suma
	return numbers

goku=[1,2,3,4]
print('Goku fase ',0,'=',goku)
for i in range(10000): goku=increaseKi(goku)
print('Goku fase ',10000,'=',goku)

