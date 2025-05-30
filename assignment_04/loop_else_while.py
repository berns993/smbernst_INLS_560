number = 1

while number <= 5:
   if number == 3:
       print("Found number 3!")
       break
   print(f"Checked {number}")
   number += 1
else:
   print("Number 3 was not found.")

#Outcome
'''
Checked 1
Checked 2
Found number 3!
'''