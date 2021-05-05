#this will help figure some shit out to do with hardware


import random
import time



#    boards.write(new+"\n")
#print(random.choice(open("boards.txt").readlines()))




boards = open("boards.txt", "a")
sensors = open("sensors.txt", "a")
userin = open("input.txt", "a")
sysout = open("output.txt", "a")
verbs = open("verbs.txt", "a")
noun = open("noun.txt", "a")




def project():

    """ main menu """
    print("______:options:_______ \n"
          "1]  Choose what to do \n"
          "2]  Enter new item \n"
          "3]  See item categories \n"
          "99] Quit \n")
    choice = input("Pick an option.->: ")
    if choice == "1":
        print(choice1())

    if choice == "2":
        print(choice2())

    if choice == "3":
        print(choice3())

    if choice == "99":
        print("goodbye -_-")
        return


def choice1():
    """generate what you want to do"""
    print("Now finding a project for you...")
    time.sleep(3)
    print("\nuse a " + random.choice(open("boards.txt").readlines()) + " with a " + random.choice(open("sensors.txt").readlines()) +
          " and pass it " + random.choice(open("input.txt").readlines()) + " input,\nand it will give you " +
          random.choice(open("output.txt").readlines()) + " output. It will " + random.choice(open("verbs.txt").readlines()) +
          " to " + random.choice(open("noun.txt").readlines()))
    print(project())


def choice2():
    boards1 = open("boards.txt", "r")
    sensors1 = open("sensors.txt", "r")
    userin1 = open("input.txt", "r")
    sysout1 = open("output.txt", "r")
    verbs1 = open("verbs.txt", "r")
    noun1 = open("noun.txt", "r")

    """ allows you to edit the lists """
    print("_____:options:_____ \n"
          "1]  Dev boards \n"
          "2]  Sensor suite \n"
          "3]  What you put in \n"
          "4]  What it gives you \n"
          "5]  What action it will do \n"
          "6]  What it will do it to \n"
          "99] Main menu \n")

    edit = input("Choose an option.->: ")
    if edit == "1":
        print("Enter a new board\n")
        board = input("->: ")
        if board not in "boards.txt":           #checks to see if what you are trying to add is in the file or not
            boards.write("\n"+board)            #writes to txt file
            print("your new board has been added!;P\n")
            print(question())                   #asks yes or no go to line 135 for function


    elif edit == "2":
        print("Enter a new sensor\n")
        sensor = input("->: ")
        if sensor not in "sensors.txt":
            sensors.write("\n"+sensor)
            print("your sensor has been added!;P")
            print(question())


    elif edit == "3":
        print("Enter a new interacton\n")
        action = input("->: ")
        if action not in "input.txt":
            userin.write("\n"+action)
            print("new action successfully added!;P")
            print(question())


    elif edit == "4":
        print("Enter a new output\n")
        out = input("->: ")
        if out not in "output.txt":
            sysout.write("\n"+out)
            print("new output added!;P")
            print(question())


    elif edit == "5":
        print("Enter a new action\n")
        act = input("->: ")
        if act not in "verbs.txt":
            verbs.write("\n"+act)
            print("action successful!XD")
            print(question())


    elif edit == "6":
        print("Enter a new object\n")
        obj = input("->: ")
        if obj not in "noun.txt":
            noun.write("\n"+obj)
            print("horton hears a new whooooo????")
            print(question())


    elif edit == "99":
        print(project())                #loops back to main menue


def question():
    print("would you like to add more?\n")
    Q = input("Y for yes N for no\n"
              "->: ")
    if Q == 'Y' or Q == 'y':
        print(choice2())

    else:
        print(project())





print(project())



