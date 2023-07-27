import random

def gameWin(Comp, you):
    if Comp == you:
        return None
    elif Comp == 'w':
        return False
    elif you == 'g':
        return True
    elif Comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif Comp == 'g':
        if you == 's':
            return False
        elif you =='w':
            return True


        if you == 'w':
            return False

print("Comp Turn: Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1,3)
if randNo == 1:
    Comp = 's'
elif randNo == 2:
    Comp = 'w'
elif randNo == 3:
    Comp = 'g'

you=input("Your Turn: Snake(s) Water(w) or Gun(g)?")
a = gameWin(Comp, you)

print(f"Computer choose {Comp}")
print(f"You choose {you}")
if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")