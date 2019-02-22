import menu

def create_an_item():
    number = int(input('Enter a number: '))
    name = input('Enter a name: ').capitalize()
    description = input('Enter a description: ').capitalize()
    ingredient = input('Enter ingredient: ').capitalize()
    price = input('Enter a price:$ ')
    menu.create_menu(number, name, description, ingredient, price)

def display_menu():
    menu_list = menu.get_menu()
    for item in menu_list:
        print(item)

def delete_menu_item():
    number = int(input('Enter the meal number: '))
    menu.delete_menu(number)
    
choices = {
    "1" : create_an_item,
    "2" : display_menu,
    "3" : delete_menu_item,
    "4" : exit
}

while True:
    print('welcome To Komodo Cafe')
    user_input = input('1. Create Menu\n' +
                    '2. View Menu\n' +
                    '3. delete Menu\n' +
                    '4. Exit\n')
    action = choices.get(user_input)
    if action:
        action()
    else:
        print("Input not valid")


   