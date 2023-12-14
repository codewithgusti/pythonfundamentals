
from engine_inheritance import Engine,ElectricEngine,VsEngine

class Car:
    engine_cls = Engine
    def __init__(self):
        # HAS-A relationship
        self.engine = self.engine_cls()
        
    def start(self):
        print('Starting engine {0} for car {1}...Wroom !, Wroom !'.format(self.engine.__class__.__name__,self.__class__.__name__))
        self.engine.start()
        
    def stop(self):
        self.engine.stop()

class RaceCar(Car):
    engine_cls= VsEngine

class CityCar(Car):
    engine_cls = ElectricEngine
# IS-A RaceCar and also Car relationship 
class F1Car(RaceCar):
    pass

car = Car()
raceCar = RaceCar()
cityCar = CityCar()
f1Car = F1Car()
cars = [car,raceCar,cityCar,f1Car]

for car in cars:
    car.start() 