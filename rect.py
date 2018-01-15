def rect(xc,yc,x1,y1,x2,y2):
	return xc>x1 and xc<x2 and yc>y1 and yc<y2
					
print(rect(2.1,2.1,1,1,2,2))