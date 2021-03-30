## Multiplication using 2 algorithms
## 1. Basic third grade algorithm || traditional algorithm
import math
import timeit

class basic:
	def __init__(self,n):
		self.no = n
		if type(self.no)!=int:
			self.no = int(self.no)

	def __mul__(self, ob):
		sum = 0
		for i,x in enumerate(reversed(str(ob.no))):
			sum = sum + (10**i)*(int(x)*self.no)
		return sum

## 2. karatsuba algorithm
def karatsuba(x, y):
	## base case
	if len(str(x))<5 and len(str(y))<5:
		return x*y

	n = int(max(math.log(x,10)+1, math.log(y,10)+1))//2
	a=x//10**n
	b=x%10**n
	c=y//10**n
	d=y%10**n

	ac = karatsuba(a,c)
	bd = karatsuba(b,d)
	abcd = karatsuba((a+b), (c+d))
	
	pwr = 10**n
	
	return pwr*pwr*ac + pwr*(abcd - ac - bd) + bd 


if __name__=='__main__':

	n1 = input()
	n2 = input()

	# default
	start = timeit.default_timer()
	print("Direct : {} ".format(int(n1)*int(n2)))
	stop = timeit.default_timer()
	print("Time : {} \n\n".format(stop-start))
	
	# 3rd grade traditional algorithm
	start = timeit.default_timer()
	print("By traditional algorithm : {}".format(basic(n1)*basic(n2)))
	stop = timeit.default_timer()
	print("Time: {} \n\n".format(stop-start))

	## Karatsuba Algorithm
	start = timeit.default_timer()
	print("By Karatsuba algorithm : {}".format(str(karatsuba(int(n1), int(n2)))))
	stop = timeit.default_timer()
	print("Time: {} \n\n".format(stop-start))