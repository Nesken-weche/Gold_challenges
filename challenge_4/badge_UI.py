import Komodo_insurance

def Add_Badge():
    badgeID = int(input('Enter Badge ID: '))
    door_access = input('Enter Door Number: ')
    Komodo_insurance.add_badge(badgeID, door_access)

def View_Badge():
    badge_list = Komodo_insurance.View_All_Badges()
    print(badge_list)

def Update_Badge():
    View_Badge()
    user = input('what is your badgeID: ')
    n = Komodo_insurance.update_Door_Access(user)


choices = {
    "1" : Add_Badge,
    "2" : View_Badge,
    "3" : Update_Badge,
    "4" : exit
}

while True:
    print('welcome To Komodo Insurance')
    user_input = input('1. Add Badge\n' +
                    '2. Badge List\n' +
                    '3. Update Badge\n' +
                    '4. Exit\n')
    action = choices.get(user_input)
    if action:
        action()
    else:
        print("Input not valid")