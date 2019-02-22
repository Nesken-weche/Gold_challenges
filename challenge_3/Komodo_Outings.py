
import outings

outing_List = []

def Add_Outings(eventType, attendees, date, total_cost_per, total_cost_event):
    o = outings.Outing(eventType, attendees, date, total_cost_per, total_cost_event)
    outing_List.append(o)
        
def View_Outings():
    if len(outing_List) > 0:
        return outing_List
    else:
        return 

def event_cost(eventType):
    total = 0
    for event in outing_List:
        if event.eventType == eventType:
            total += event.total_cost_event
    return total



