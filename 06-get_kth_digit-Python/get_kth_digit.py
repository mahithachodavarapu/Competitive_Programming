# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(digit, k):
	l=[]
	if(k>=len(str(digit))):
    		return 0
	digit=abs(digit)
	while(digit):
		l.append(digit%10)
		digit=digit//10
	return l[k]
#print(fun_get_kth_digit(-789,1))		
