import random

print("Hej !")
print("Zagrajmy w grę!")

name = input("Jak masz na imie?: ")

print("Witaj "+ name+ "!")

game = ['kamień', 'papier', 'nożyczki']

user_input= ""
score = 0
while user_input!="Q":
    random_number = random.randint(0,2)
    comp_input= game[random_number]
    user_input= input("\nWybierz kamień / papier / nożyczki /  Q aby wyjść: ")
    
    #if user_input == "Q":
     #    break  
    
    if user_input not in game:
        print("Wybór niepoprawny\nWybierz jeszcze raz !")
        continue     
    
    # print("Komputer wybrał: " + comp_input)
    # print(f"Komputer wybrał: {comp_input}")
    # print("Użytkownik wybrał: "+ user_input)
    print(f"\tKomputer wybrał: {comp_input} \n\tUżytkownik wybrał: {user_input}")

    cond = [user_input == "papier" and comp_input == "kamień",\
    user_input == "kamień" and comp_input == "nożyczki",
    user_input == "nożyczki" and comp_input == "papier"]

    wygrana = any(cond) 


    if user_input == comp_input:
        print("\nRemis :)")
    elif wygrana:
        print("Wygrałeś :) ")
        score = score + 1

    # ta część kodu może być wykorzystana jeśłi nie zastosujemy zmiennej cond 
    # elif user_input == "papier" and comp_input == "kamień":
    #     print("Wygrałeś !")
    # elif user_input == "kamień" and comp_input == "nożyczki":
    #     print("Wygrałeś !")
    # elif user_input == "nożyczki" and comp_input == "papier":
    #     print("Wygrałeś !")
    else:
        print("Przegrałeś :(")
        score -=1
    print(f"Masz {score} punktów")

