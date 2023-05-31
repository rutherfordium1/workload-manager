def generate_sorted_numbers(n):
    numbers = list(range(1, n+1))
    return sorted(numbers)

# Get input from the user
number = int(input("Enter a number: "))

# Generate and print the sorted numbers within the range
sorted_numbers = generate_sorted_numbers(number)
print("Sorted numbers within the range:")
print(sorted_numbers)
