import random


def gameWin(comp,you):
  if comp == you:
    return None

  elif comp =='s':
    if you == 'w':
      return False
    elif you == 'g':
      return True

  elif comp == 'w':
    if you == 's':
      return True
    elif you == 'g':
      return False

  elif comp == 'g':
    if you == 's':
      return False
    elif you == 'w':
      return True
    

    

print("Comp  turns : Snake(s),Water(w),Gun (g) : " )
r= random.randint(1,3)
#print(r)

if(r == 1):
  comp= 's'
elif r == 2:
  comp= 'w'
elif r == 3:
  comp= 'g'




you=  input("Your  turns : Snake(s),Water (w),Gun(g)")

a=gameWin(comp,you)

print(f"Computer Chose : {comp}")
print(f"You Chose : {you}")
print()

if a == None:
  print("The game is tie")
elif a == True:
  print("Congratulations :( You Won !! ")
else :
  print("Oops :( Computer Wins ")