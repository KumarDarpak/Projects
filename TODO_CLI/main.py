"""
What we need 
Welcome to TODO 
Is there any task : (Yes or No ?)
Yes --> No


-Yes 
Hello User !
If list is empty 
    -  want to add or Exit
        want to Add append in the list 
    - exit break;
-No
Nothing to Do! Now you're Relaxed! Send Yes To use Add a Task

"""
yesContainer = ["yes", "ys", "s", "hell yeah", "han", "hanji", "ha"]
noContainer = ["no", "nah", "none", "on", "hell no", "nope"]

taskContainer = []

print("Welcome to the TODO CLI 📝")
inp = input("Is there are any Task : (Yes or No ?)")

def taskAdder(taskToAdd):
    taskContainer.append(taskToAdd)
    for ind, val in taskContainer:
        print(f"{ind} -> {val} \t")

if inp.lower() in yesContainer:
    while (inp.lower() != "exit"):
        if (inp.lower() in noContainer):
            print("Feeww! No task Available")
        else:
            inpTask = input("What's your task ?\t")
            taskContainer.append(inpTask)
            print("for removal ")
            if taskContainer :


else:
    print("Please Select Yes or No")

