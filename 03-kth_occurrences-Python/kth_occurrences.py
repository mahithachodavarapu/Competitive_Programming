# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.



def fun_kth_occurrences(s, n):
	d={}
	l=[x for x in s]
	for i in s:
		d[i]=l.count(i)
	#print(d)
	for i in range(n-1):
		m=max(d, key=d.get)
		d.pop(m)
		#print(d)
	return max(d,key=d.get)
	
			
print(fun_kth_occurrences("hsdibdouvbeiovbfeibvdsioubidsbvviefadbcildfab", 4))	
#v		


