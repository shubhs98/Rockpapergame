import random
def gamewin(comp,player2):
    if comp==player2:
        return None
    elif comp=='s':
        if player2=='w':
            return False
        elif player2=='g':
            return True
    elif comp=='w':
        if player2=='g':
            return False
        elif player2=='s':
            return True

    elif comp=='g':
        if player2=='s':
            return False
        elif player2=='w':
            return False


print("COMP TURN: snake(s) water(w) gun(g)")
randno = random.randint(1,3)

if randno==1:
    comp='s'
elif randno==2:
    comp='w'
elif randno == 3:
    comp='g'

player2 = input("YOUR TURN: snake(s) water(w) or gun(g)\n")

a = gamewin(comp,player2)
if a==None:
    print("tie")
elif a==True:
    print("you win")
else:
    print("you lose")