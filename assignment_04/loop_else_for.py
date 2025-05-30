numbers = [1, 2, 4, 5]

for num in numbers:
   if num == 3:
       print("Found number 3!")
       break
   print(f"Checked {num}")
else:
   print("Number 3 was not found.")

#Outcome
'''
Checked 1
Checked 2
Checked 4
Checked 5
Number 3 was not found.
'''