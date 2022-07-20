import os.path
import re
import pyodbc


def a_function(first, last, age):
    if 18 > age:  # if age lower then 18
        print("Hi, ", '\033[1m' + first.capitalize(), last.capitalize() + '\033[0m'", comeback when you have 18")
        d_function()
    else:  # if age higher then 18
        print("Hi, ", '\033[1m' + first.capitalize(), last.capitalize() + '\033[0m'", do you like to continue ?")
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
    first = Firstname
    last = Lastname
    print("See you next time", '\033[1m' + first.capitalize(), last.capitalize() + '\033[0m')
    global Mycoins
    sql2 = f"UPDATE t_coins SET coins = '{Mycoins}' WHERE id = 1;"
    cursor.execute(sql2)
    cursor.commit()
    exit()


def e_function(result):
    if result:  # If b_function result equals True then initial c_function
        c_function()
        global selectmenu
        selectmenu = 1  # var selectmenu equals 1 (main menu)
        if os.path.isfile('teste.txt'):
            f = open("teste.txt", "r")
            global Mycoins
            Mycoins = f.read()
        else:
            f = open("teste.txt", "w")
            f.write("0")

        option = OptionValidation_function(selectmenu)
        return option
    else:  # If b_function result equals False then initial c_function
        d_function()  # exit


def f_function(choose):
    match choose:  # Check Option Choose by the user and return the respective function
        case '1':
            g_function()  # initial design Insert Coin menu
            global selectmenu
            selectmenu = 2  # var selectmenu equals 2 (Insert Coin menu)
            option = OptionValidation_function(selectmenu)
            return menu_function(selectmenu, option)
            # returns function to user input "choose" do the respective
            #                                           menu functions
        case '2':
            return print("Gambling")  # Check Option Choose by the user and return the respective function
        case '3':
            h_function()  # initial design Insert Coin menu
            selectmenu = 4  # var selectmenu equals 2 (Insert Coin menu)
            option = OptionValidation_function(selectmenu)
            return menu_function(selectmenu, option)  # returns function to user input "choose" do the respective
            #                                           menu functions
        case '4':
            return d_function()  # exit


def g_function():  # Insert Coin Menu design
    global coin1, coin2, coin3
    print("-----------------------")
    print(" CASINO - Insert Coin  ")
    print("-----------------------")
    print(" ")
    print(coin1)
    print(coin2)
    print(coin3)
    print("Back - Press 4")
    print(" ")
    print("-----------------------")
    print("-----------------------")


def menu_function(selectedmenu, choose):
    if selectedmenu == 2:  # Check what menu was entered
        match choose:  # Check Option Choose by the user and return the respective function
            case '1':
                AddCoins_function(choose)  # Check Option Choose by the user and return the respective function
            case '2':
                AddCoins_function(choose)  # Check Option Choose by the user and return the respective function
            case '3':
                AddCoins_function(choose)  # Check Option Choose by the user and return the respective function
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
    option = OptionValidation_function(selectmenu)
    return f_function(option)  # returns f_function to user input "choose" do main menu functions


def h_function():  # View My Coins Menu design
    global Mycoins
    print("-----------------------")
    print("   CASINO - My Coins   ")
    print("-----------------------")
    print(" ")
    print("My coins - ", Mycoins)
    print("Back - Press 1")
    print(" ")
    print("-----------------------")


def age_function():  # Validation Age Input
    while True:
        age = input("Age : ")
        try:
            val = int(age)  # Transform Input to INTEGER, to do the validation
            if val >= 0:  # If option is above 0
                break  # Goes directly to the return
            else:
                print("Age can't be negative, try again")  # input is a negative number
        except ValueError:  # If input is not a INTEGER
            print("Age must be a number, try again")  # input is not a number
    return val


def OptionValidation_function(selectedmenu):  # Validation Options Inputs
    if selectedmenu in (1, 2):  # Validation Input in first menu and second menu because is the same number of option
        while True:
            option = input("Choose : ")
            try:
                val = int(option)  # Transform Input to INTEGER, to do the validation
                if val in (1, 2, 3, 4):  # If option is inside 1, 2, 3, 4 (Options Available)
                    break  # Goes directly to the return
                else:
                    print("Option need to be 1, 2, 3 or 4, try again")  # input is not inside the list of options
            except ValueError:  # If input is not a INTEGER
                print("Option must be a number inside 1, 2, 3 or 4, try again")  # input is not a number
        return str(val)  # Returns STRING because we are working in other functions this value in string
    elif selectedmenu == 4:  # Validation Input in fourth menu , only one option available
        while True:
            option = input("Choose : ")
            try:
                val = int(option)  # Transform Input to INTEGER, to do the validation
                if val == 1:  # If option is 1 (Only Option Available)
                    break  # Goes directly to the return
                else:
                    print("The only option available is 1, try again")  # input is not inside the list of options
            except ValueError:  # If input is not a INTEGER
                print("Option must be the number 1, try again")  # input is not a number
        return str(val)  # Returns STRING because we are working in other functions this value in string


def AddCoins_function(option):
    global Mycoins, coin1, coin2, coin3
    match option:  # Check Option Choose by the user and return the respective function
        case '1':
            value = getInt_function(coin1)
            Mycoins = int(Mycoins) + value
            return backToMain()
        case '2':
            value = getInt_function(coin2)
            Mycoins = int(Mycoins) + value
            return backToMain()
        case '3':
            value = getInt_function(coin3)
            Mycoins = int(Mycoins) + value
            return backToMain()


def getInt_function(value):
    return int(re.search(r'\d+', value).group())


def getDataSql_function():
    comando = "SELECT coins FROM t_coins"
    cursor.execute(comando)
    sql = cursor.fetchone()
    int(getInt_function(str(sql)))
    return int(getInt_function(str(sql)))

Firstname = input("Firstname : ")  # Firstname user
Lastname = input("Lastname : ")  # Lastname user
y = "YES"  # var y represents YES
n = "NO"  # var n represents
selectmenu: int = 1  # Menu selection
coin1: str = "10000 Coins - Press 1"
coin2: str = "1000 Coins - Press 2"
coin3: str = "100 Coins - Press 3"
dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-J6T9HAV\SQLEXPRESS;"
    "Database=teste;"
)
conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

Mycoins = getDataSql_function()


AgeVerify = age_function()  # Validation Input Age

resultA = a_function(Firstname, Lastname, AgeVerify)  # Check Age

resultB = b_function(resultA.upper(), y)  # Check if user want to continue

optionChoose = e_function(resultB)  # if user say yes continue, if no End program

f_function(optionChoose)  # Program check what option the user made (1, 2, 3 or 4)
