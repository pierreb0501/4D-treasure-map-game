# name: Pierre Andre El Boustany
# McGill ID: 261076411

ROOM_NAME = "Chainsaw man"
AUTHOR = "Pierre Andre El Boustany"
PUBLIC = True 

BLUE_LIGHT = False
PAINTING_MESSAGE = False
FINISH = False
MOVE = 0
choice = int

def room_description(): 
    ''' () -> NoneType
    Prints a description of the room 
    '''
    print ("You entered the MOST DANGEROUS PLACE ON EARTH! The chamber of the Chainsaw man!\nIt is very difficult to escape this hell but with resilience, focus and patience it's possible.\nYou hear the footsteps of the monsters next to the main door.\nYour time is limited which means a total of 5 moves !\nYou see a lot of different structures such as a table, a cupboard, a magic box and a painting with only 1 exit : a door. \nGood luck!\nTIPS: by entering list commands you can see all the available options")
        
def cupboard():
    ''' () -> NoneType
    Prints what happen when you interact with the cupboard
    '''
    print ("OMG !!! A dead body !!! What a monster ... if I don't find the exit fast I will probably be the next corpse. I should hurry up and search somewhere else. ")
    
def painting():
    ''' () -> NoneType
    Takes user's input
    Prints what happen when you interact with the painting
    '''
    global PAINTING_MESSAGE
    global BLUE_LIGHT
    if PAINTING_MESSAGE == False : #first time interacting with the painting
        print ("Even the painting is horrific, it gives me the chills. If I look at it one more time I will probably throw up, I should probably destroy it...WAIT! Seems like something is written on the wall behind the painting, I should maybe find something to see more clearly.")
        PAINTING_MESSAGE = True  #the painting has already been examined and the secret is revealed 
    elif PAINTING_MESSAGE == True and BLUE_LIGHT == True : #if the painting has already been examined and the blue light retrieved
        print ("I hope I will be able to see the thing written on the wall with the blue light, let's try. Fantastic! It's working! D E A T and H ... Oh, welcoming ... ")
    elif PAINTING_MESSAGE == True and BLUE_LIGHT == False: #if the painting has already been examined and the blue light not retrieved
        print ("Surely it's possible to read the message, I just need a kind of lamp or something")

def box():
    ''' () -> NoneType
    Takes user's input
    Prints what happen when you interact with the box
    '''
    global BLUE_LIGHT #I imported the constant to use it in the function and to change the inventory depending on the player's decision
    if BLUE_LIGHT == False: #first time interacting with the box
        print ("PLEASE DON'T EAT MY HAND! PLEASE DON'T EAT MY HAND! PLEASE DON'T EAT MY HAND! ... looks safe to me ... WOW SMOKE COMING FROM THE BOX!!! Should I remove my hand or keep it ???")
        decision = str(input("what will I do ? :"))
        if "remove" in decision : 
            print ("THAT was terrifying ... never again. Let's check something less creepy. ")
        elif "keep" in decision : 
            print ("OK OK OK! I GOT THIS ! AAAAAHHHHHH aaaaahhhhh aaahhh ah ... something dropped in my hand, a blue light ? Might be useful I guess , I didn't risk my hand for nothing.")
            BLUE_LIGHT = True #you know have the blue light in your possession
        else :
            print ("THIS IS NOT AN OPTION! THINK FAST!!")
    elif BLUE_LIGHT == True: #the blue light has already been retrieved
        print ("I already retrieved the item in the box + a heart attack so no thanks. I can use it in another place maybe")

def table():
     ''' () -> NoneType
    Prints what happen when you interact with the table
    '''
     print ("just a bunch of knives and human organs ... normal stuff to have at home huh? Maybe I should take a picture of this for proof if I ever get out alive.")

def door():
    ''' () -> NoneType
    Takes user's input
    Prints what happen when you interact with the door
    '''
    global FINISH
    print ("I need to enter a code of 5 letters to exit ")
    code = str(input("The code is :")) #enter the code 
    if code == "DEATH": 
        print ("YESSSSSS FINALLYYYYY !!!! Now ... Where am i supposed to go ?")
        FINISH = True #if the code is correct, end the escape (the program)
    else:
        print ("NOPE! I have to search better.")

def list_commands():
    ''' () -> NoneType
    Prints all the available commands
    '''
    print ("examine the cupboard \nexamine the table \nexamine the painting \nexamine the box \nexamine the door ")

def number_moves():
    ''' () -> NoneType
    count and prints the number of moves left
    '''
    global MOVE
    global FINISH
    if MOVE == 0 :
        print("6 moves left")
    elif MOVE == 1:
        print("5 moves left")
    elif MOVE == 2:
        print("4 moves left")
    elif MOVE == 3:
        print("3 moves left")
    elif MOVE == 4:
        print("2 moves left")
    elif MOVE == 5:
        print("1 last move")
    elif MOVE == 6:
        print("NO MORE CHANCES! The CHAINSAW MAN enters the room and is ready to play with his new toy... YOU LOSE ! Try again?")
        
    
        
    
def escape_room():
    ''' () -> NoneType
    Takes user's input
    Prints a consequence depending on the user's inputs and decisions through all the other functions
    '''
    global FINISH
    global PAINTING_MESSAGE
    global BLUE_LIGHT
    global MOVE
    room_description()
    while FINISH == False : #the escape continues until you enter the code
        number_moves()
        choice = str(input("next move :"))
        choice = choice.lower() 
        if "cupboard" in choice :
            cupboard()
        elif "painting" in choice : 
            painting()
        elif "box" in choice :
           box()
        elif "table" in choice :
            table()
        elif "door" in choice :
            door()
        elif choice == "list commands":
            list_commands()
        else:
            print("please enter a valid action")
            
        if MOVE == 5:
            print("NO MORE CHANCES! The CHAINSAW MAN enters the room and is ready to play with his new toy... YOU LOSE ! Try again?")
            break
        
        MOVE = MOVE + 1
        
        
        
        
    
    





     