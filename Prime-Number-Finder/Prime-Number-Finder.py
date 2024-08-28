def prime_finder(n):
	prime_list = []
	for num in range(1, n+1):
		factor_list = []
		for factor in range(1, num+1):
			if num % factor ==0:
				factor_list.append(factor)
		if len(factor_list) == 2:
			prime_list.append(num)
	return prime_list

print(prime_finder(11))
