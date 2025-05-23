#Recipe for a delicious meal mad lib

'''
adj
container
number
ingredients
adj2
spice
kitchen tool
adj3
noun
'''

#testing it out with inputs too...
adj = input("Adjective: ")
container = input("Choose a vessel: ")
number = input("Number: ")
ingredients = input("Ingredients: ")
adj2 = input("Adjective: ")
spice = input("Spice: ")
kitchen_tool = input("Choose a tool: ")
adj3 = input("Adjective: ")
noun = 'tasty'

story = (f'''
Recipe for a delicious meal mad lib
         
Today, we're going to make a {adj} dish! First, take a large 
{container} and fill it with {number} cups of {ingredients}. 
Then, add a {adj2} pinch of {spice} and stir it all together. 
Once the mixture is smooth, heat up your {kitchen_tool} and 
cook everything until it looks {adj3}. Finally, serve it on a 
plate and garnish with {noun} for the perfect finish!
''')

print(story)