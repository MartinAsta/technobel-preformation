'''
Commencez par créer une liste de 10 nombres aléatoires compris entre 1 et 100. Ensuite, affichez cette liste générée.
Après cela, calculez la somme de tous les éléments de la liste et affichez-la.
'''
import random
def ex1():
    list_of_randoms = [random.randint(1,100) for _ in range(10)]
    print(list_of_randoms)

    sum_of_randoms = sum(list_of_randoms)
    print(sum_of_randoms)

'''
Invitez l'utilisateur à saisir son prénom et son nom. Ensuite, créez un tuple contenant ces informations. Pour finir,
affichez séparément le prénom et le nom à partir du tuple.
'''
def ex2():
    first_name = input("What is your first name ? : ")
    last_name = input("What is your last name ? : ")
    identity = (first_name, last_name)
    print(f"Your first name is {identity[0]} and your last name is {identity[1]}.")

'''
Générez deux ensembles de nombres aléatoires compris entre 1 et 20. Affichez ces deux ensembles générés. Enfin,
trouvez l'intersection des deux ensembles et affichez-la.
'''
def ex3():
    set1 = set()
    set2 = set()
    for _ in range(10):
        set1.add(random.randint(1,20))
        set2.add(random.randint(1,20))
    intersection = set1.intersection(set2)
    print(intersection)

'''
Créez un dictionnaire contenant les prix de quelques fruits tels que la pomme, la banane et l'orange. Demandez à
l'utilisateur de saisir le nom d'un fruit, puis affichez le prix correspondant à ce fruit s'il existe dans le dictionnaire
'''
def ex4():
    fruits = {
        "apple" : 1,
        "banana" : 1.1,
        "orange" : 0.5
    }
    request = input("What fruit would you like ? : ")
    price = fruits.get(request)
    answer = f"Your {request} will cost {price}€." if price else f"We do not sell any {request}, sorry !"
    print(answer)

'''
Créez une liste de tuples contenant le nom et l'âge de trois personnes. Trouvez ensuite la personne la plus âgée et
affichez son nom.
'''
def ex5():
    persons = [("Martin", 28),("Ana",21),("Antoine",29)]
    oldest = max(persons, key=lambda p:p[1])
    print(oldest[0])

'''
Générez une liste de 10 nombres aléatoires compris entre 1 et 50. Affichez cette liste générée. Ensuite, filtrez les
nombres pairs de la liste et créez une nouvelle liste ne contenant que ces nombres pairs. Enfin, affichez la nouvelle
liste contenant uniquement les nombres pairs.
'''
def ex6():
    list_of_randoms = [random.randint(1,50) for _ in range(10)]
    print(list_of_randoms)
    even_randoms = [n for n in list_of_randoms if n%2 == 0]
    print(even_randoms)

'''
Créez une liste de mots contenant des doublons. Transformez ensuite cette liste en un ensemble pour éliminer les
doublons. Affichez l'ensemble résultant.
'''
def ex7():
    list_of_words = ["oui","oui","non","ok","ok","ahok"]
    print(set(list_of_words))

'''
Créez un dictionnaire de listes représentant différents cours et les étudiants inscrits dans chaque cours. Ajoutez des
étudiants à chaque cours. Ensuite, demandez à l'utilisateur de saisir le nom d'un cours et affichez la liste des
étudiants inscrits à ce cours.
'''
def ex8():
    classes = {
        "Math" : ["Martin", "Ana", "Bob", "Alice"],
        "History" : ["Killian", "Trevor", "Greg", "Celia"],
        "Music" : ["Jessica", "Audrey", "Sam", "Anabelle"]
    }
    class_requested = input("For which class do you need to see the list of students ? : ")
    list_of_students = classes.get(class_requested)
    answer = f"For the class of {class_requested}, the students are {list_of_students}." if list_of_students else "We do not teach that class."
    print(answer) 

'''
Créez une liste de tuples représentant les commandes d'achat avec les produits et les quantités. Ensuite, créez un
dictionnaire de prix pour chaque produit. Calculez ensuite le coût total de toutes les commandes et affichez-le.
'''
def ex9():
    orders = [("apple",10),("orange",6),("banana",20),("apple",3),("banana",35),("orange",99),("orange",1)]
    fruits = {
        "apple" : 1,
        "banana" : 1.1,
        "orange" : 0.5
    }

    cost = sum([x[1] * fruits.get(x[0]) for x in orders])
    print(cost)

'''
Créez une liste de dictionnaires représentant les informations des employés avec leur nom, salaire et département.
Calculez la somme des salaires pour chaque département, puis calculez la moyenne des salaires pour chaque
département. Enfin, affichez les moyennes des salaires pour chaque département.
'''
def ex10():
    employees = [
        {
            "Name" : "Martin",
            "Salary" : 2,
            "Department" : "IT"
        },
        {
            "Name" : "Ana",
            "Salary" : 1000,
            "Department" : "Literature"
        },
        {
            "Name" : "Thomas",
            "Salary" : 1,
            "Department" : "IT"
        },
        {
            "Name" : "Chantal",
            "Salary" : 2000,
            "Department" : "Administration"
        },
        {
            "Name" : "Catherine",
            "Salary" : 1999,
            "Department" : "Administration"
        },
        {
            "Name" : "Anthonin",
            "Salary" : 5,
            "Department" : "Research"
        }
    ]
    depart_count = [x.get("Department") for x in employees]
    depart_count = set((x,depart_count.count(x)) for x in depart_count)
    average_salaries = {}
    for employee in employees:
        if average_salaries.get(employee.get("Department")):
            average_salaries[employee.get("Department")] += employee.get("Salary")
        else:
            average_salaries[employee.get("Department")] = employee.get("Salary")
    for d,c in depart_count:
        average_salaries[d] /= c
    print(average_salaries)
 