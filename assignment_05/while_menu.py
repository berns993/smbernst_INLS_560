menu_option = ''

while menu_option != 'q':
    print('MENU:', 'a: fried tomatoes', 'b: pimiento cheese', 'q: quit', sep="\n")
    menu_option = input("Enter a letter for more info about the restuarant offerings: ")
    if menu_option == 'a':
        print('Tomatoes are in season. These are fried fresh and served with ranch.')
    elif menu_option == 'b':
        print("A classic staple! Nothing like spreading some over some crackers with pickles.")