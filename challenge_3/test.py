
import unittest
import Komodo_Outings 

class TestOuting(unittest.TestCase):

    def test_Add_Outing_should_add_Outing(self):
        self.eventType = 'eventType'
        self.attendees = 'attendees'
        self.date = 'date'
        self.total_cost_per = 'total_cost_per'
        self.total_cost_event = 'total_cost_event'

        #act
        Komodo_Outings.Add_Outings(self.eventType, self.attendees, self.date, self.total_cost_per, self.total_cost_event) 
        actual = len(Komodo_Outings.outing_List)
        expected = 1

        #assert
        self.assertEqual(expected, actual)

    def test_View_Outings_should_view_list(self):
        #arrange
        #act
        actual = len(Komodo_Outings.outing_List) 
        expected = 1 
        #assert
        self.assertEqual(expected, actual)

    def test_event_cost_should_give_Cost_Per_Event(self):
        # Arange
        eventType = 'golf'
        attendees = 100
        date = 'date'
        total_cost_per = 100
        total_cost_event = 10000
        Komodo_Outings.Add_Outings(eventType, attendees, date, total_cost_per, total_cost_event)


        expected = 10000
        actual = Komodo_Outings.event_cost("golf")
        #act
        self.assertEqual(expected, actual)
