#just making it human readable

#backslash '\' is a line continuation character. It is going out of style
long_variable_1 = 1 + 3 + 4 + \
1 + 3 + 4

#parentheses also keeps information together, it is not a touple in this instance
long_variable_2 = (1 + 3 + 400 + 1 
+ 3 + 4)

#the list does not always have to be on one line as long as its in brackets
list = ["orange", "banana", "apple"]

list2 = [
        "cat", 
        "dog",
        "mouse"
        ]

#dictionary
my_dictionary = {
        "age": 10, 
        "name": "Bill",
        "Job": "carpenter"
        }
#numbers do not have to be in quotes

#print(my_dictionary)
#output: {'age': 10, 'name': 'Bill', 'Job': 'carpenter'}

print(my_dictionary, list2)
#output: {'age': 10, 'name': 'Bill', 'Job': 'carpenter'} ['cat', 'dog', 'mouse']