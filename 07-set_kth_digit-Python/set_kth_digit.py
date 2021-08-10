# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
		li=[]
		while(abs(n)):
			li.append(n%10)
			n=n//10
		if(k>len(li)):li.insert(k,d)
		else:
			li[k]=d
		c=1
		num=0
		for i in li:
			num+=i*c
			c=c*10
		return num  			
			
#print(fun_set_kth_digit(468, 3, 1))
