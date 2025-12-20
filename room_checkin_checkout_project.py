def check_in():
    visitors = {}
    total_rooms = 2
    for rooms in range(total_rooms):
        names = input('name: ')
        room = input('room: ')
        visitors[names] = (room)
        print(f'{visitors[names]} is checked in at {room}')
        selection = input('Check in Another? Y/N')
        for choice in selection:
            match choice:
                case 'y.lower()':
                    continue
    return (room and visitors)

def check_out():
    

def menu():
    print('''
+-----------------------------------------+
| Welcome To Check in/ Check Out Service  |
| 1. View Current Rooms In Use            |
| 2. Check In An Individual               |
| 3. Check Out An Individual              |
| Type 'exit' in any Menu to go back      |
+-----------------------------------------+
            ''')
    selection = input('> ' )
    for choice in selection:
        match choice:
            case '1':
                pass
            case '2':
                check_in()
            case 3:
                pass

menu()