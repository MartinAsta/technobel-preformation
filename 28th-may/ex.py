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
import time
import threading
class Car():
    def __init__(self, brand:str, model:str, min_speed:float, max_speed:float):
        self.__brand = brand
        self.__model = model
        self.__min_speed = min_speed
        self.__max_speed = max_speed

    def get_speed(self) -> float:
        return self.__min_speed + (self.__max_speed - self.__min_speed) * random.random()
    
    @property
    def brand(self):
        return self.__brand
    
    @property
    def model(self):
        return self.__model

def exercise(laps:int, lap_length:float) -> None:
    cars = [Car("Ford","model1",40,80),
            Car("Audi","model2",60,75),
            Car("Porsche","model3",65,70),
            Car("BMW","model4",30,90)]
    threads = []

    for car in cars:
        t = threading.Thread(target=race, args=(laps,lap_length,car))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

def race(laps:int, lap_length:float, car:Car) -> None:
    total_time = 0
    for i in range(laps):
        speed = car.get_speed()
        lap_time = (lap_length / speed) * 3600
        total_time += lap_time
        lap_time_minutes = lap_time // 60
        lap_time_secondes = lap_time - lap_time_minutes * 60
        time.sleep(lap_time)
        print(f"The {car.brand} {car.model} finished the lap {i+1} in {int(lap_time_minutes)} minutes and {int(lap_time_secondes)} seconds !")
    total_time_minutes = total_time // 60
    total_time_seconds = total_time - total_time_minutes * 60
    print(f"The {car.brand} {car.model} finished the race in {int(total_time_minutes)} minutes and {int(total_time_seconds)} seconds !")

exercise(5,1)