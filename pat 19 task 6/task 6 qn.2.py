def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

original_list = [10, 501, 22, 37, 100, 999, 87, 351]

prime_numbers = []

for num in original_list:
    if is_prime(num):
        prime_numbers.append(num)

print("Prime Numbers:", prime_numbers)