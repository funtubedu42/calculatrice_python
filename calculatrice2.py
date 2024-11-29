import colored
from colored import Fore, Back, Style

x = 0
y = 0
t = 0
exit = True

print(f"{Style.reset}     **Bienvenue sur la calculatrice !**     ")
print(f"{Style.reset}                    [V2]                     ")

while exit:
    x = float(input(f"{Style.reset}choisi le premier nombre : "))
    a = input(f"{Style.reset}choisi l'opération : ")
    y = float(input(f"{Style.reset}choisi le deuxième nombre : "))
    
    if a == "-" :
        t = x - y
    
    elif a =="+":
        t = x + y
    
    elif a =="*":
        t = x * y

    elif a =="/":
        if y == 0:
            print(f"{Fore.red}{Back.red}❌ Division pas zéro impossible !")
        else :
            t = x / y
    else :
        print(f"{Back.orange_4b}⚠️  Ce n'est pas une opération valide !")
    if not a == 0 :
        print(f"{Style.reset}", x,a,y,"=", t)

    choice = input(f"{Style.reset}arrêter de calculer ? y/n : ")

    if choice == "y":
        exit = False
        print(f"🔴 Calculatrice{Fore.red} arrêtée ! {Style.reset}")