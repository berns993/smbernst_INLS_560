menu_option = ''

while menu_option != 'q':
    print(f'''
'MENU:',
'a: fried tomatoes',
'b: pimiento cheese',
'q: quit'
''')
    menu_option = input("Enter a letter for more info about the restuarant offerings: ")
    if menu_option == 'a':
        print('Tomatoes are in season. These are fried fresh and served with ranch.')
    elif menu_option == 'b':
        pimiento = input('Would you like the pimiento? enter (y or n): ').lower()
        if pimiento == 'y':
            print("Great! I will put that in for you now.")
        else:
            print("No worries! What else catches your fancy?")