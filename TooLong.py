n=eval(input())
words=[]

for i in range (n):
	n=input()
	words.append(n)
if len(n)<10:
	print (n)
else : 
	beforelastchar=len(n)-2
	lastchar=n[len(n)]
	print (n[0],end="")
	print (n[1,beforelastchar],end="")
	print (n[lastchar],end="")
