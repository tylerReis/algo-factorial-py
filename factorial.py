def factorial(num):
	answer = 1
	while num > 0:
		answer = answer * num
		num = num - 1
	return answer

print(factorial(8))