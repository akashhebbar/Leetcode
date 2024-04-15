def is_armstrong(num):
    # Calculate the number of digits
    temp = num
    num_digits = 0
    while temp > 0:
        num_digits += 1
        temp //= 10

    # Calculate the sum of the digits raised to the power of num_digits
    temp = num
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** num_digits
        temp //= 10

    # Check if the total is equal to the original number
    return total == num


# Example usage:
number = 153
if is_armstrong(number):
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")
