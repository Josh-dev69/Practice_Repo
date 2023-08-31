def is_prime(num):
    if num <= 1: return False
    if num <= 3: return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    else: return True

for i in range(1, 50):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
