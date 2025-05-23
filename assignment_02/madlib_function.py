# Mad lib example for functions. 

def madlib(adj, container, number, ingredients, adj2, spice, kitchen_tool, adj3, noun):
    ''
    '''Mad lib using a function'''
    story = (f'''
    Recipe for a delicious meal mad lib
            
    Today, we're going to make a {adj} dish! First, take a large {container} and fill it with {number} cups of {ingredients}.   Then, add a {adj2} pinch of {spice} and stir it all together. Once the mixture is smooth, heat up your {kitchen_tool} and cook everything until it looks {adj3}. Finally, serve it on a plate and garnish with {noun} for the perfect finish!
    ''')
    return story

#commenting out the below, needed before "with input" 
#print(madlib('adj', 'shoe', 'five', 'onions', 'green', 'nutmeg', 'whisk', 'crisp', 'watch'))

#with input
def get_input():
    adj = input("Adjective: ")
    container = input("Choose a vessel: ")
    number = input("Number: ")
    ingredients = input("Ingredients: ")
    adj2 = input("Adjective: ")
    spice = input("Spice: ")
    kitchen_tool = input("Choose a tool: ")
    adj3 = input("Adjective: ")
    noun = input("Noun: ")
    return adj, container, number, ingredients, adj2, spice, kitchen_tool, adj3, noun

inputs = get_input()
print(madlib(*inputs))