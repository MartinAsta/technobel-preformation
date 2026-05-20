'''
Créez un programme qui gère les commandes de café en fonction des différentes options telles que la taille, le type de
café, les extras, etc. Utilisez des correspondances pour traiter chaque option et calculer le prix total de la commande.
'''
def ex1(type:str, size:str, sugar:bool=False, milk:bool=False) -> float:
    price = 0
    match type:
        case "espresso":
            price += 2
        case "long":
            price += 2.5
        case "short":
            price += 1.75
        case _:
            return -1
    match size:
        case "small":
            price += 1
        case "medium":
            price += 2
        case "large":
            price += 4
        case _:
            return -1
    
    if sugar:
        price += 0.5
    if milk:
        price += 0.5
    return price

'''
Créez un programme qui convertit une note numérique en une note alphabétique en utilisant une échelle de notation
standard. Utilisez des correspondances pour déterminer la note alphabétique correspondante en fonction de la note
numérique
'''
def ex2(note:float) -> float:
    if note < 10:
        return "Echec"
    elif note < 12:
        return "Réussite"
    elif note < 14:
        return "Satisfaction"
    elif note < 16:
        return "Distinction"
    elif note < 18:
        return "Grande distinction"
    else:
        return "La plus grand distinction"

'''
Créez un programme qui génère un nombre aléatoire (import random) et permet à l'utilisateur de deviner ce nombre.
Utilisez des correspondances pour comparer la devinette de l'utilisateur avec le nombre généré et fournir des indices.
'''
import random
def ex3() -> str:
    r = random.randint(1,10)
    while True:
        guess = int(input("Devine entre 1 et 10 ? "))
        if guess == r:
            return "Bravo"
        elif guess < r:
            print("C'est plus !")
        else:
            print("C'est moins !")

'''Créez un programme qui calcule l'indice de masse corporelle (IMC) d'une personne en fonction de son poids et de sa
taille. Utilisez des correspondances pour interpréter et catégoriser l'IMC résultant en différentes catégories de poids.
'''
def ex4(weight:float, height:float) -> float:
    bmi = weight/height**2
    print(f"Your BMI is {bmi} !")

    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Healthy weight"
    elif bmi < 30:
        return "Overweight"
    elif bmi < 35:
        return "Obesity class 1"
    elif bmi < 40:
        return "Obesity class 2"
    else:
        return "Obesity class 3"

'''
Créez un programme qui permet à l'utilisateur de choisir un menu pour chaque repas (petit-déjeuner, déjeuner, dîner)
parmi des options préétablies. Après la sélection, il affiche les choix de l'utilisateur pour chaque repas et résume
l'ensemble des repas de la journée.
'''
def ex5() -> list:
    breakfast_choices = ["Muesli", "pancakes", "idk", "water"]
    lunch_choices = ["lunch1", "lunch2", "lunch3"]
    dinner_choices = ["Pizza","Pasta","Raviolis"]
    day = []

    print(breakfast_choices)
    choice = int(input("Which option do you want ? "))
    day.append(breakfast_choices[choice-1])

    print(lunch_choices)
    choice = int(input("Which option do you want ? "))
    day.append(lunch_choices[choice-1])

    print(dinner_choices)
    choice = int(input("Which option do you want ? "))
    day.append(dinner_choices[choice-1])

    return day


'''
Créez un programme qui génère des citations aléatoires à partir d'un nombre aléatoire. L'utilisateur devrait pouvoir
choisir un thème et le programme générera une citation aléatoire correspondante. Utilisez des correspondances pour
gérer les différents thèmes et générer les citations appropriées.
'''
def ex6(theme:str) -> str:
    motivational_quotes = ["Oui", "Bravo c'est bien", "Tu peux le faire"]
    idkman_quotes = ["a","b","c"]
    oui_quotes = ["oui", "yes","da", "ja", "po", "si"]
    quote:str

    match theme:
        case "motivational":
            quote = motivational_quotes[random.randint(0,len(motivational_quotes) - 1)]
        case "idk":
            quote = idkman_quotes[random.randint(0,len(idkman_quotes) - 1)]
        case "oui":
            quote = oui_quotes[random.randint(0,len(oui_quotes) - 1)]
        case _:
            return "Pick 'motivational', 'idk' or 'oui'."
    return quote

'''
Concevez un programme qui génère et affiche les nombres premiers jusqu'à 100 en utilisant une boucle.
'''
def ex7() -> None:
    print(2,sep=" ", end=" ")
    for i in range(3,101,2):
        flag = True
        for j in range(3,i//2):
            if i%j == 0:
                flag = False
                pass
        if flag:
            print(i, end=" ")

'''
Créez un programme qui demande à l'utilisateur d'entrer son âge. Utilisez un opérateur ternaire pour vérifier si
l'utilisateur est majeur ou mineur. Affichez ensuite un message approprié en fonction de la réponse.
'''
def ex8(age:int) -> str:
    return "You're a minor" if age < 18 else "You're major"

'''
Jeu de devinette de nombre amélioré : Écrivez un jeu interactif où l'ordinateur génère un nombre aléatoire entre 1 et
100, et l'utilisateur doit deviner ce nombre. Utilisez une boucle pour permettre à l'utilisateur de faire plusieurs
tentatives. Après chaque tentative, demandez à l'utilisateur s'il souhaite continuer à jouer. Répétez le processus
jusqu'à ce qu'il décide de ne plus jouer. Enfin, affichez le nombre de tentatives utilisées pour deviner le nombre
'''
def ex9() -> int:
    total_guesses:int = 0
    number_to_guess = random.randint(1,100)
    keep_playing = True
    while keep_playing:
        guess = int(input("Guess a number between 1 and 100 : "))
        total_guesses += 1
        if guess == number_to_guess:
            print("Bravo")
            return total_guesses
        elif guess < number_to_guess:
            print("It's more")
        else:
            print("It's less")
        
        keep_playing = True if input("Do you wanna keep playing ? (y/n) : ") == "y" else False

    return total_guesses

'''
Écrivez un programme qui demande à l'utilisateur d'entrer un mot. Utilisez une boucle pour afficher chaque caractère
du mot un par un jusqu'à la fin du mot.
'''
def ex10() -> None:
    word_to_spell_out:str = input("What's the word you want to spell out ? : ")
    for i in word_to_spell_out:
        print(i)

'''
Gestionnaire de commandes de café amélioré :Écrivez un programme interactif qui prend les commandes de café en
fonction des options telles que la taille, le type de café et les extras. Utilisez une boucle pour permettre à l'utilisateur
de passer plusieurs commandes et affichez le prix total à la fin de chaque commande. Demandez ensuite à l'utilisateur
s'il souhaite passer une autre commande et répétez le processus jusqu'à ce qu'il n'en ait plus envie.
'''
def ex11() -> int:
    total_price:int = 0
    type = input("Espresso, long or short ? : ")
    size = input("Small, medium or large ? : ")
    sugar = True if input("sugar ? (y/n) : ") == "y" else False
    milk = True if input("milk ? (y/n) : ") == "y" else False
    total_price += ex1(type, size, sugar, milk)

    want_more = True if input("more ? (y/n) : ") == "y" else False
    if want_more:
        total_price += ex11()
    return total_price

'''
Écrivez un programme qui demande à l'utilisateur d'entrer un mot. Utilisez une boucle pour inverser l'ordre des lettres
du mot et affichez le mot inversé à la fin.
'''
def ex12() -> None:
    word_to_revert = input("Mot à inverser ?")
    for i in range(len(word_to_revert)-1,-1, -1):
        print(word_to_revert[i],end="")

'''
Gestion des repas du jour améliorée : Développez un programme interactif qui permet à l'utilisateur de choisir un menu
pour chaque repas de la journée parmi des options prédéfinies. Utilisez une boucle pour faciliter la saisie des choix
pour chaque repas et affichez un résumé des choix de repas à la fin. Demandez ensuite à l'utilisateur s'il souhaite
choisir les repas pour un autre jour. Répétez le processus jusqu'à ce qu'il décide de ne plus choisir de repas.
'''
def ex13() -> list:
    diet = []
    diet.append(ex5())

    another_day = True if input("Wanna set another day ? (y/n) : ") == "y" else False
    while another_day:
        diet.append(ex5())
        another_day = True if input("Wanna set another day ? (y/n) : ") == "y" else False
    return diet

'''
Combien de possibilités de recouvrement y a-t-il en connaissant n ? Sur une bande de 2 mètres sur n mètres sachant que chaque dalle fait 2x1
mètres
'''
def challenge(n:int) -> int:
    if n == 0 or n == 1:
        return n*2
    
    total, first, last = 0,0,1
    for i in range(0, n+1):
        total = first + last
        last = first
        first = total
    return 2**n * total

for i in range(11):
    print(challenge(i)) #0 2 8 