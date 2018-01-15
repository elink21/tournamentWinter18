def inverted(escene):
	for i in range(len(escene)):
		for j in range(len(escene[0])):
			if(escene[i][j]==2 or escene[i][j]==3):
				number=escene[i][j]
				escene[i][j]=0
				x=i
				while(escene[x-1][j]!=1 or x>0):
					if(escene[x-1][j]==1):
						escene[x][j]=number
						break
					x-=1
	return escene


escene=[
[1,1,1,1,1,1,1],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,1,1,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[3,3,3,3,3,3,3],
[1,1,1,1,1,1,1]
]

for line in escene:print (line)
new= inverted(escene)
print()
print()
for line in new:print (line)