def egg_drop(n):
	count = 0
	target = n
	while target > 0:
		count += 1
		target -= count
	return count

print(egg_drop(100))
print(egg_drop(36))
