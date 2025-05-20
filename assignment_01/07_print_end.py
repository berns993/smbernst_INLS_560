#link: https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/

#From the site, default
print("Welcome to")
print("GeeksforGeeks")
#creating a visual separator
print("-----------")

#with end
print("Welcome to", end = ' ')
print("GeeksforGeeks", end= ' ')

#output
'''
Welcome to
GeeksforGeeks
-----------
Welcome to GeeksforGeeks 
'''

#testing
print("Welcome to", end = ' my ')
print("GeeksforGeeks", end= ' ')
#output: Welcome to my GeeksforGeeks