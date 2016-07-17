n=eval(input())
words=[]

for i in range (n):
	n=input()
	words.append(n)
	if len(n)<10:
		print (n)
	else : 
		beforelastchar= len(n)-1
		lastchar=n[len(n)-1]
		print (n[1],n[1,beforelastchar],n[lastchar])
