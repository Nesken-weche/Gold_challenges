
import menu_item 

menu_list = []
def create_menu(number, name, description, ingredient, price):
    m = menu_item.Menu_Item(number, name, description, ingredient, price)
    menu_list.append(m)

def get_menu():
    return menu_list
 
def delete_menu(number):
    for Menu_Item in menu_list:
        if Menu_Item.number == number: 
            index = menu_list.index(Menu_Item)
            menu_list.pop(index)
            return True
