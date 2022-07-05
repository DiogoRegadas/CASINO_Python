Firstname = input("Firstname : ")  # Firstname user
Lastname = input("Lastname : ")  # Lastname user
Age = int(input("Age : "))  # Age user
y = "YES"  # var y represents YES
n = "NO"  # var n represents
selectmenu: int = 1  # Menu selection


def a_function(first, last, age):
    if 18 > age:  # if age lower then 18
        print("Hi, ", first.capitalize(), last.capitalize(), ", comeback when you have 18")
        d_function()
    else:  # if age higher then 18
        print("Hi, ", first.capitalize(), last.capitalize(), ", do you like to continue ?")
        result = input("Yes or No ? : ")  # if you want to leave or stay

        while result.upper() != y and result.upper() != n:  # if input result not equals yes or no, repeat input
            result = input("Yes or No ? : ")
        return result


def b_function(text, stat1):
    if text == stat1:  # If says yes from a_function then return True
        result: bool = True
    else:  # If says no from a_function then return False
        result: bool = False
    return result


def c_function():  # Main Menu design
    print("-----------------------")
    print("        CASINO         ")
    print("-----------------------")
    print(" ")
    print("Insert Coins - Press 1")
    print("Gambling - Press 2")
    print("My Coins - Press 3")
    print("Exit - Press 4")
    print(" ")
    print("-----------------------")


def d_function():  # Exit program function
    print("See you next time")
    exit()


def e_function(result):
    if result:  # If b_function result equals True then initial c_function
        c_function()
        global selectmenu
        selectmenu = 1  # var selectmenu equals 1 (main menu)
        choose = int(input("Choose : "))
        return choose
    else:  # If b_function result equals False then initial c_function
        d_function()  # exit


def f_function(choose):
    match choose:  # Check Option Choose by the user and return the respective function
        case '1':
            g_function()  # initial design Insert Coin menu
            global selectmenu
            selectmenu = 2  # var selectmenu equals 2 (Insert Coin menu)
            choose = input("Choose : ")
            return menu_function(selectmenu, choose)  # returns function to user input "choose" do the respective
            #                                           menu functions
        case '2':
            return print("Gambling")  # Check Option Choose by the user and return the respective function
        case '3':
            h_function()  # initial design Insert Coin menu
            selectmenu = 4  # var selectmenu equals 2 (Insert Coin menu)
            choose = input("Choose : ")
            return menu_function(selectmenu, choose)  # returns function to user input "choose" do the respective
            #                                           menu functions
        case '4':
            return d_function()  # exit


def g_function():  # Insert Coin Menu design
    print("-----------------------")
    print(" CASINO - Insert Coin  ")
    print("-----------------------")
    print(" ")
    print("10000 Coins - Press 1")
    print("1000 Coins - Press 2")
    print("100 Coins - Press 3")
    print("Back - Press 4")
    print(" ")
    print("-----------------------")


def menu_function(selectedmenu, choose):
    if selectedmenu == 2:  # Check what menu was entered
        match choose:  # Check Option Choose by the user and return the respective function
            case '1':
                return print("Gambling")  # Check Option Choose by the user and return the respective function
            case '2':
                return print("Gambling")  # Check Option Choose by the user and return the respective function
            case '3':
                return print("Coins")  # Check Option Choose by the user and return the respective function
            case '4':
                return backToMain()  # Back to main menu
    elif selectedmenu == 3:
        match choose:  # Check Option Choose by the user and return the respective function
            case '1':
                return print("Gambling")  # Check Option Choose by the user and return the respective function
            case '2':
                return print("Gambling")  # Check Option Choose by the user and return the respective function
            case '3':
                return print("Coins")  # Check Option Choose by the user and return the respective function
            case '4':
                return backToMain()  # Back to main menu
    elif selectedmenu == 4:
        match choose:  # Check Option Choose by the user and return the respective function
            case '1':
                return backToMain()  # Back to main menu


def backToMain():  # Back to main menu
    c_function()  # Recreate main menu
    global selectmenu
    selectmenu = 1  # Assign selectmenu equals 2 (Insert Coin menu)
    choose = input("Choose : ")
    return f_function(choose)  # returns f_function to user input "choose" do main menu functions


def h_function():  # View My Coins Menu design
    print("-----------------------")
    print(" CASINO - My Coins     ")
    print("-----------------------")
    print(" ")
    print("My coins - ")
    print("Back - Press 1")
    print(" ")
    print("-----------------------")


resultA = a_function(Firstname, Lastname, Age)  # Check Age

resultB = b_function(resultA.upper(), y)  # Check if user want to continue

optionChoose = e_function(resultB)  # if user say yes continue, if no End program

f_function(optionChoose)  # Program check what option the user made (1, 2, 3 or 4)
