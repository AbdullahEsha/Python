table = {'dirty':'suck the dust', 'clean': 'move'}


def leftright(current_location):
    if current_location == 'A':
        return 'Right'
    elif current_location == 'B':
        return 'Left'
    
def lookup(percept):
    for i in table:
        if i == percept[1]:
            return table[i]
        
def table_agent(percept):
    action = lookup(percept)
    if action == 'move':
        action = leftright(percept[0])
    print(action)
    
ch = 'y'
while ch != 'n':
    room_name = input('Enter room name (A/B):')
    room_status = input('Enter room status (dirty/clean):')
    percept = [room_name, room_status]
    table_agent(percept)
ch = input('wish to continue (y/n):')