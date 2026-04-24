def start_adventure():
    print("You go to sleep one night and you wake up to multiple people taking you from your house." \
    "You wake up again but this time you are in a dark basement. ")
    print("There is a door at the top of the stairs and there is a window right above the bed but it is borded up." \
    "What do you do first?")
    print("1. You go try to open the door at the top of the stairs")
    print("2. You go try to pry the boards off the window")
    print("3. You look around the room for somthing that could help you escape")
    print("4. You sit there hopelessly and do nothing.")

    choice_1 = input(">")

    if choice_1 == "1" :
        try_door()
    elif choice_1 =="2":
        try_window()
    elif choice_1 == "3":
        look_around()
    elif choice_1 == "4":
        do_nothing()
    else:
        print("Invalid choice. Try again")
    
def basement():
    print("1. You go try to open the door at the top of the stairs")
    print("2. You go try to pry the boards off the window")
    print("3. You look around the room for somthing that could help you escape")
    print("4. You sit there hopelessly and do nothing.")
    choice = input(">")
    if choice == "1":
          print(" You have tried the door too many times and the captors find you.")
    elif choice == "2" :
          try_window()
    elif choice == "3" :
          look_around()
    elif choice == "4" :
          do_nothing()
    
          


def do_nothing():
         print("You do nothing and eventually the captors come downstairs to finish you off. You lose")

    
def try_window():
            print("The boards are too strong for you to take off without a tool. You sit back down on the bed")
            print("1.You go try to open the door at the top of the stairs")
            print("2. You look around the room for somthing that could help you escape")
            print("3. You sit there hopelessly sit there and do nothing.")
            choice = input(" >")
            if choice == "1":
                 print("The door is locked and you have to go back downstairs")
                 basement()
            elif choice == "2":
                  look_around()
            elif choice == "3":
                  do_nothing()

def open_window():
      print(" You have the crowbar and can now open the window and get outside")
def outside():
      print("You are now outside and in the backyard. There is a fence surronding the complex. " \
      "What do you decide to do?")
      print("1. Try to climb the fence. ")
      print("2. You try to walk out of the front gate.")
      print("3. Look around the area for somthing to help you.")
      choice = input(" >")
      if choice == "1" :
            print(" The fence is electric and when you touch it you get shocked and the captors find you passed out." "You lose.")
      elif choice == "2" :
            print(" You try the front gate and no one sees you and you end up escaping the complex.")
            road()
      elif choice == "3" :
            print(" You end up finding wire cutters.")
            fence()                

def look_around():
            print("You end up finding a crowbar. You use that to break the boards off the window and escape the basement")
            outside()
def fence() : 
      print(" With the wire cutters you decide to cut a hole in the fence.")
      find_captors()


def find_captors() :
      print(" You get through the hole but you end up finding gaurds surronding the area. What do you do next?")
      print("1. Try to sneak around them.")
      print("2. You wait to see if there is a opening for you to try to escape.")
      print("3. You try to look around for somthing to help you.")
      choice = input(" >")
      if choice == "1" : 
            print(" You were not sneaky enough and they caught you. You lose.")
      elif choice == "2" :
            print("You end up waiting and you see a opening to get past them.")
            road()
      elif choice == "3" :
            print(" You dont find anything useful.")
            find_captors()
        
def road():
      print(" You end up getting out of the complex but you are now stranded on a road and don't know where you are. What do you do?")
      print("1. Look around for somthing to help you.")
      print("2. Wait for a car to pass by and see if they can help you.")
      print("3. Start walking down the road and see where it leads you")
      print("4. Wait to see if anything happens.")
      choice = input(" >")
      if choice == "1" :
            print("You end up finding a discarded map.")
            map_()
      elif choice == "2" :
            print("A car ends up passing by but you can't flag them down and they don't see you") 
            road()
      elif choice == "3" :
            print(" You end up getting horrible lost and you can't find your way back. You lose.")
      elif choice == "4" :
            print(" Nothing happens.")
            road()
     
def map_() :
      print(" The map you find is a map of the area. You use that to start walking toward the nearest town. When you get close to town the map cuts off and there is a fork in the raod. What do you do?")
      print("1. Take a left")
      print("2. Take a right.")
      choice = input(" >")
      if choice == "1" :
            print(" This path ends up taking you to town")
            town()
      elif choice == "2" : 
            print(" This path takes you a abondond mine shaft.")  
            mine_shaft()
        

def mine_shaft() :
      print(" You end up at a mineshaft. What do you do?")
      print("1. Go back to the fork in the road.")
      print("2. Go into the mineshaft.")
      print("3. Sit and do nothing.")
      choice = input(" >")
      if choice == "1" :
            map_()
      elif choice == "2" :
            print(" You go into the mineshaft and the mineshaft collapses on you. You die.")  
      elif choice == "3" :
            print(" You do nothing and eventually it gets dark and you get attacked by a bear and die. You lose.")



def town() :
      print(" You get to the town. What is the first thing you do?")
      print("1. Ask someone for help.")
      print("2. Go into a store and try to buy somthing.")
      print("3. Look around for somthing to help you.")
      choice = input(" >")
      if choice == "1" :
            print(" You try to ask for help but no one helps you")
            town()
      elif choice == "2" :
            store()
      elif choice == "3" :
            print(" You end up finding a map of where you are on a wall. You take it and start following it to where you think is home.")
            map_2()



def map_2():
      print("You start walking on the path, but you see are car broken down on the side of the road. What do you do?")
      print("1. Go try and help them.")
      print("2. Hide and see what the person in the car is doing.")
      print("3. Try to steal the car.")
      print("4. Mind you own bussines and keep walking.")
      choice = input(" >")
      if choice == "1" :
            print(" As you walk up to the person they hop out of the car and shoot you. You lose.")
      elif choice == "2" :
            print(" You try to hide but they see you and shoot you. You lose.")
      elif choice == "3" :
            print(" That was stupid, the person comes out and shoots you.You lose.")
      elif choice == "4" :
            print(" You keeo following the path and you don't bother the person in the car.")
            home()


def home() :
      print(" You end up making it home after following the path all the way. You win")


              
def store() :
      print("You are in the store. What do you do?")
      print("1. Try to steal somthing.")
      print("2. Try to talk to an employee there.")
      print("3. Leave.")
      choice = input(" >")
      if choice == "1" :
            print(" One of the store employees see you stealing and they call the cops on you and you get arrested. You lose")
      elif choice == "2" :
            print(" You talk to an employee and they show you where the police station is.")
            police_station()
      elif choice == "3" :
            town()

def try_door():
        print(" The door is locked and you have to go back downstairs")
        print("1. You go try to pry the boards off the window")
        print("2. You look around the room for somthing that could help you escape")
        print("3. You sit there hopelessly sit there and do nothing.")
        choice_2 = input (">")  
        if choice_2 == "1":
            print(" The boards are too strong for you to take off without a tool. You sit back down on the bed")
            basement()
        elif choice_2 == "2":
            print("You end up finding a crowbar. You could use that for good use.")
            basement()
        elif choice_2 == "3":
            print("You do nothing.")
            basement()
        else: print("Invalid choice. Try again")
        try_door

def police_station():
      print("You are now at a police station. What do you do?")
      print("1. Tell them what happend to you.")
      print("2. leave")
      choice = input(" >")
      if choice == "1":
            print(" You tell them what happened and they end up bringing you back home. But they don't end up finding the captors. You win.")
      elif choice == "2" :
            town()

start_adventure()