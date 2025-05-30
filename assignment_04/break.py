# Divisible by 7? Find first
numbers = [12, 23, 34, 45, 56, 67]

for num in numbers:
    if num % 7 == 0:
        print(f"Divisible by 7: {num}")
        break
    print(f"Processing: {num}")

#Outcome (compare to continue.py)
'''
Processing: 12
Processing: 23
Processing: 34
Processing: 45
Divisible by 7: 56
'''