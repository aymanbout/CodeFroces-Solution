words=[]
n=eval(input())
for i in range (n):
  	n=input()
  	words.append(n)
  	if len(n)<10:
  		print (n)
  	else:
  		x=len(n)
  		numofchar= n[1,x-1]
  		lastchar=x-2
  		print(n[0],numofchar,lastchar)
