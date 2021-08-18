# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	if(n==0):return 0
	l=[]
	while(n):
		l.append(n%10)
		n=n//10
	s=set(l)
	d={}
	for i in s:
		d[i]=l.count(i)
	
	
	return max(d, key=d.get)
			
	
"""
(24, 2),
	(0, 0),
	(26011, 1),
	(14, 1),
	(2, 2),
	(5, 5),
	(5231123123123, 1),
	(5312312355565, 5),
	(1102300, 0)
"""	
print(mostfrequentdigit(1102300))