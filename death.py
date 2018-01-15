def clean(names):
	x=['light','kira']
	filter=''
	copy=''
	i=0
	while i < len(names):
		filter=''
		print(i)
		
		if(names[i]==x[0][0]):
			for z in range( i, i+len(x[0])  ):
				filter+=names[z]
			print(filter)
			if filter==x[0] :
				i+=len(x[0])-1
				print("match:",i)
			else :copy+=names[i]
		filter=''
		if(names[i]==x[1][0]):
			for z in range( i, i+len(x[1])  ):
				filter+=names[z]
			print(filter)
			if filter==x[1] :
				i+=len(x[1])-1
				print("match:",i)
			else :copy+=names[i]
		else: copy+=names[i]
		i+=1
	return copy
print(clean(input()))
