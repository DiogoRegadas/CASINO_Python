Firstname = input("Firstname : ")
Lastname = input("Lastname : ")
Age = int(input("Age : "))
cont = ""


def a_function(first, last, age):
    if 18 > age:
        print("Hi, ", first, last, ", comeback when you have 18")
    else:
        print("Hi, ", first, last, ", do you like to continue ?")
        result = input("Yes or No ? : ")
        result.upper()
        return result


checkAge = a_function(Firstname, Lastname, Age)

print(checkAge)
