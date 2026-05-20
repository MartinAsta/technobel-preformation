def ex1():
    first_name = input("Prénom ?")
    last_name = input("Nom ?")

    print(first_name, last_name, sep=":)")

def ex2():
    phrase1, phrase2 = "Salut !", "Ca va ?"
    print(phrase1, phrase2, sep=" :)\n", end=" :)\n")

def ex3():
    m1, m2 = input("Premier mot ?"), input("Deuxième mot ?")
    print(m1,m2, sep="")

def ex4():
    n1, n2 = int(input("Nombre 1 ?")), int(input("Nombre 2 ?"))
    print(n1+n2, end=" Bravo")

def ex5():
    val1, val2, val3 = "Oui", "Non", "Ok"
    print(val1,val2,val3, sep="_", end=" fin")

def ex6(n1:int, n2:int):
    saved = n1
    n1 = n2
    n2 = saved
    print(n1, n2)

def ex7(n:int):
    days = n//86400
    n -= days * 86400
    hours = n//3600
    n -= hours * 3600
    minutes = n//60
    n -= minutes * 60

    print(f"{days} jours {hours} heures {minutes} minutes et {n} secondes")