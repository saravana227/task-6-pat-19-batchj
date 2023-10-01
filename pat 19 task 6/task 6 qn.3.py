def is_happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

original_list = [10, 501, 22, 37, 100, 999, 87, 351]

happy_numbers = [num for num in original_list if is_happy_number(num)]
count_happy_numbers = len(happy_numbers)

print("Happy Numbers:", happy_numbers)
print("Number of Happy Numbers:", count_happy_numbers)