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

def sum_of_prime_factors(n):
	primes_between = prime_finder(n)
	prime_factors = []
	for prime in primes_between:
		if n % prime == 0:
			prime_factors.append(prime)
	total = sum(prime_factors)
	return total

print(sum_of_prime_factors(91))
