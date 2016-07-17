words=[]  #creating a list 
n=eval(input())
for i in range (n):
  	n=input()
  	words.append(n)
  	if len(n)<=10:
  		print (n)
  	else:
  		x=len(n)
  		numofchar= x-2
  		lastchar=n[-1]
  		resulat=str(n[0])+str(numofchar)+str(lastchar)
  		print(resulat,end="\n")
