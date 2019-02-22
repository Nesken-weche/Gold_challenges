
class Badge:

    def __init__ (self, badgeID, door_access):
        self.badgeID = badgeID
        self.door_access = door_access

    def __repr__ (self):
        return f'{self.badgeID}- {self.door_access}'

    def remove_doors(self):
        remove_doors = []

    def remove_door(self):
        remove_door = Badge('badgeid', 'door_access')

    def add_door(self):
        add_door = Badge('badgeid', 'door_access')

if __name__ == "__main__":
    test = Badge('0000', '#A7')
    print(test)


