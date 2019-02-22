
import unittest
import menu

class TestMenu(unittest.TestCase):

    def test_create_menu_should_create_menu(self):
        self.number = 'number'
        self.name = 'name'
        self.description = 'description'
        self.ingredient = 'ingredient'
        self.price = 'price'

        #act
        menu.create_menu(self.number, self.name, self.description, self.ingredient, self.price)
        actual = len(menu.menu_list)
        expected = 1

        #assert
        self.assertEqual(expected, actual)

    def test_get_menu_should_display_menu(self):
        #arrange
        #act
        actual = len(menu.get_menu())
        expected = 1 
        #assert
        self.assertEqual(expected, actual)

    def test_menu_delete_menu_menu_should_delete(self):
        #arrange
        self.number = 'number'
        self.name = 'name'
        self.description = 'description'
        self.ingredient = 'ingredient'
        self.price = 'price'
        #act
        menu.create_menu(self.number, self.name, self.description, self.ingredient, self.price)
        self.assertTrue(menu.delete_menu(self.number))