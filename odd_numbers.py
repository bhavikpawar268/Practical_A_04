# Odd Numbers between 1 to 50

odd_numbers = [num for num in range(1, 51) if num % 2 != 0]

print("Odd Numbers:", odd_numbers)
print("Three Minimum Odd Numbers:", odd_numbers[:3])
print("Three Maximum Odd Numbers:", odd_numbers[-3:])
print("Average of Odd Numbers:", sum(odd_numbers) / len(odd_numbers))