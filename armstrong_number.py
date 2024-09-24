"""When a sum of the individual digits of a number is raised to the power of 4 and the sum is equal to the original number itself, 
such a number is known as an Armstrong number."""



def armstrong_number(n):

	l = list(str(n))
	power = len(l)

	final_sum = 0
	
	for i in range(0,power):
		temp_sum = pow(int(l[i]),power)
		final_sum+=temp_sum


	if final_sum == n:
		print(f"{n} is an armstrong number")
	else:
		print(f"{n} is not an armstrong number")


#armstrong_number(123)
#armstrong_number(8208)






