def sum_of_first_and_last_digit(number):
    # Ensure the number is positive
    number = abs(number)
    
    # Convert the number to a string to easily extract the digits
    number_str = str(number)
    
    # Check if the number has only one digit
    if len(number_str) == 1:
        return 2 * number
    
    # Extract the first and last digits and convert them back to integers
    first_digit = int(number_str[0])
    last_digit = int(number_str[-1])
    
    # Calculate the sum of the first and last digits
    return first_digit + last_digit

# Input an integer
num = int(input("Enter an integer: "))

# Calculate and print the sum of the first and last digits
result = sum_of_first_and_last_digit(num)
print("Sum of the first and last digit:", result)