
import Komodo_Outings

def Add_Event():
    eventType = input('Enter an Event: ') 
    attendees = int(input('Enter the number of people attending: ')) 
    date = int(input('Enter a date: ')) 
    total_cost_per = int(input('Enter cost per person: $ ')) 
    total_cost_event = total_cost_per * attendees
    Komodo_Outings.Add_Outings(eventType, attendees, date, total_cost_per, total_cost_event)

def View_Events():
    Outing_list = Komodo_Outings.View_Outings()
    for i in Outing_list:
        print(i)

def Cost_Per_Event():
    eventType = input('Enter an event: ')
    total = Komodo_Outings.event_cost(eventType)
    print(total)


choices = {
    "1" : Add_Event,
    "2" : View_Events,
    "3" : Cost_Per_Event,
    "4" : exit
}

while True:
    print('welcome To Komodo Claim Department')
    user_input = input('1. Add Event\n' +
                    '2. View Events\n' +
                    '3. Cost Per Event\n' +
                    '4. Exit\n')
    action = choices.get(user_input)
    if action:
        action()
    else:
        print("Input not valid")