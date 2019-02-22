
class Outing:
    def __init__(self, eventType, attendees, date, total_cost_per, total_cost_event):
        self.eventType = eventType
        self.attendees = attendees
        self.date = date
        self.total_cost_per = total_cost_per
        self.total_cost_event = total_cost_event

    def __repr__(self):
        return f"{self.eventType}- {self.attendees}- {self.date}- {self.total_cost_per}- {self.total_cost_event}"

if __name__ == "__main__":
    name = Outing('Golf', '150', 'month', '$15', '$2000')
    print(name)

