
class Menu_Item:
    def __init__(self, number, name, description, ingredient, price):
        self.number = number
        self.name = name
        self.description = description
        self.ingredient = ingredient
        self.price = price

    def __repr__(self):
        return f"{self.number}- {self.name.title()}- {self.description}- {self.ingredient}- {self.price}" 
        
if __name__ == "__main__":
    burger = Menu_Item('1', 'Hamburger', '20 calories', 'bread and meat', '$1')
    print(burger)
