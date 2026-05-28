'''
Un ensemble de voitures effectue une course sur un circuit, elles parcourent un nombre de tours donné.
le circuit dispose d'une distance par tour exprimée en km
Chaque voiture possède une vitesse minimale et maximale qui va nous permettre de déterminer la vitesse de la voiture à chaque tours
(de manière aléatoire)
En fonction de la vitesse de la voiture et de la distance du circuit, nous pouvons déterminer le temps que la voiture a mis pour faire son
tour du circuit.
La voiture ayant le temps total (somme de tous les temps par tour) le plus base remporte la victoire.

Pour mener à bien cet exercice, le programme principal devrait ressembler à ceci (à quelques détailes près) :
- Initialiser le nombre de tours et la distance par tour
- Créer les voitures
- Effectuer le nombre de tours donné pour toutes les voitures en (en affichant le temps au tour de chaque voiture)
- Trouver la voiture ayant le temps total le plus bas et afficher son modèle, sa marque, et son temps total.
'''
import random
def exercise(laps:int, length:float) -> None:
    total_distance = laps * length
    car1 = Car("Ford","model1",40,80)
    car2 = Car("Audi","model2",60,75)
    car3 = Car("Porsche","model3",65,70)
    car4 = Car("BMW","model4",30,90)

class Car():
    def __init__(self, brand:str, model:str, min_speed:float, max_speed:float):
        self.__brand = brand
        self.__model = model
        self.__min_speed = min_speed
        self.__max_speed = max_speed

    def calculate_timer(self, distance:float) -> float:
        return distance / self.__min_speed + (self.__max_speed - self.__min_speed) * random. random()
    
    @property
    def brand(self):
        return self.__brand
    
    @property
    def model(self):
        return self.__model

exercise(5,20)