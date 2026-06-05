"""
input 
user want to start 
then we will

"""

print("Welcome to CLI_CAL")
str = input('start/end \t')
while (str != 'end'):
    if (str == 'end'):
        print("Thank you for using the CLI_CAL \t")
    elif (str == 'start'):
        print("Which operation you want ? choose the number \t")
        for i in range(5):
            oper = '';
            if i == 0:
                oper = 'Add'
            if i == 1:
                oper = 'Subtract'
            if i == 2:
                oper = 'Multiply'
            if i == 3:
                oper = 'Divide'
            if i == 4:
                oper = 'end'
            print(f"{i + 1} -> {oper}")
        inpOper = int(input('Which operation Index \t'))
        if inpOper == 5:
            print("Thank you for using the CLI_CAL BYE :-) \t")
            break

        if inpOper == 1:
            howManyVal = int(input("How many times you wnat to add? \t"))
            finalVal = int(input("From which Number You want to Add? \t"))
            for i in range(howManyVal):
                addVal = int(input('Which number you want to add \t'))
                finalVal += addVal
                print(f"At {i + 1} {finalVal}")
            print(f"Your Final submition after Addition {finalVal} \t")
            break

        if inpOper == 2:
            howManyVal = int(input("How many times you want to Subtract? \t"))
            finalVal = int(input("From which Number You want to Subtract? \t"))
            for i in range(howManyVal):
                valToSubtract = int(input('input Please \t'))
                finalVal -= valToSubtract
                print(f"At {i + 1} {finalVal}")
            print(f"Your Final Value after Subtraction {finalVal} \t")
            break

        if inpOper == 3:
            howManyVal = int(input("How many times you want to Multiply? \t"))
            finalVal = int(input("In which Number You want to Multiply? \t"))
            for i in range(howManyVal):
                valToMultply = int(input('input Please \t'))
                finalVal *= valToMultply
                print(f"At {i + 1} {finalVal}")
            print(f"Your Final Value after Multiplication {finalVal} \t")
            break
        
        if inpOper == 4:
            howManyVal = int(input("How many times you want to Divide? \t"))
            finalVal = int(input("From which Number You want to Divide? \t"))
            if (finalVal <= 0 ):
                print('Can\'t divide from 0 May you please choose the value more than 0')
            for i in range(howManyVal):
                valToDivide = int(input('input Please \t'))
                finalVal /= valToDivide
                print(f"At {i + 1} {finalVal}")
                if (finalVal <= 0):
                    print("Can't divide from 0")
            print(f"Your Final Value after Multiplication {finalVal} \t")
            break

        else:
            print("Choose the number between 1 <-> 5 \t")
    else:
        print("Please input start or end \t")
    str = input('start/end \t')
print('\n \nThank you for using the CLI CALCULATOR :-) BYE BYE ]\n')