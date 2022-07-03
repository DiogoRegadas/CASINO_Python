Firstname = input("Firstname : ")
Lastname = input("Lastname : ")
Age = int(input("Age : "))
y = "YES"
n = "NO"
f = "False"
t = "True"


def a_function(first, last, age):
    if 18 > age:
        print("Hi, ", first, last, ", comeback when you have 18")
        d_function()
    else:
        print("Hi, ", first, last, ", do you like to continue ?")
        result = input("Yes or No ? : ")

        while result.upper() != y and result.upper() != n:
            result = input("Yes or No ? : ")
        return result


def b_function(text, stat1):
    if text == stat1:
        result: bool = True
    else:
        result: bool = False
    return result


def c_function():
    print("-----------------------")
    print("        CASINO         ")
    print("-----------------------")
    print(" ")
    print("Insert Coins - Press 1")
    print("Gambling - Press 2")
    print("Coins - Press 3")
    print("Exit - Press 4")
    print(" ")
    print("-----------------------")


def d_function():
    print("See you next time")
    exit()


def e_function(result):
    if result:
        c_function()
        choose = input("Choose : ")
        return choose
    else:
        d_function()


def f_function(choose):

    match choose:
        case 1:
            "Insert Coins"
        case 2:
            "Gambling"
        case 3:
            "Coins"
        case 4:
            return d_function()


resultA = a_function(Firstname, Lastname, Age)

resultB = b_function(resultA.upper(), y)

select = e_function(resultB)

f_function(select)
