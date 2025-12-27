import os
global toDoListPrint
toDoListPrint = []


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def toDoList():
    addingToList = True
    print('Type "view" to exit and view to do list')
    while addingToList == True:
        addChoreToList = input('>')
        toDoListPrint.append(addChoreToList)
        for items in toDoListPrint:
            match items:
                case 'view':
                    del toDoListPrint[-1]
                    addingToList = False
                    viewToDoList()

def viewToDoList():
    clear()
    sortByNumber = 1
    for items in toDoListPrint[:]:
        print(f'{sortByNumber} : {items}')    
        sortByNumber += 1
    removeTodoList()
    

def removeTodoList():  
    removingFromList = True
    print('To mark as done type corresponding\nnumber to list item.\nWhen done, type "exit"')
    while removingFromList == True:
        try:
            removeFromList = input('>')
            del toDoListPrint[int(removeFromList) - 1]
            viewToDoList()
        except ValueError:
            if removeFromList == 'exit':
                removingFromList = False
                viewToDoList()

        
        
toDoList()
        



        
             
        
    
    
    


               