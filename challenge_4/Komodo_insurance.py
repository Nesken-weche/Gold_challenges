import badge

badge_list = []

def add_badge(badgeID, door_access):
    b = badge.Badge(badgeID, door_access)
    badge_list.append(b)            

def View_All_Badges():
    if len(badge_list) > 0:
        return badge_list
    else:
        return('List is empty')

def remove_all():
    r = badge.Badge(re)

def remove_door():
    if user == badge.Badge('badgeID'):
        badge_list.pop(badge.Badge('door_access'))



def update_Door_Access(user):
    for b in badge_list:
        if badge_list.add_badge(badgeID) == user:
            print(badge_list.Badge(door_access))
        if badgeID == Badge(badgeID):
            print(Badge(door_access))
            option = input('Do you want to replace or add doors: ').capitalize()
        if option == 'Add':
            option_2 = input('Add another door: ')  
            badge_list.append(option_2)
        elif option == 'Replace':
            option_3 = input('Enter wich door: ')  
            for i in badge_list:
                if i == option_3:
                    badge_list.pop()        
        return badge_list


