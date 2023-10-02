import random

class Animal:
    def __init__(self, nombre, salud_max, hambre_max, felicidad_max):
        self.nombre = nombre
        self.salud = salud_max
        self.hambre = hambre_max
        self.felicidad = felicidad_max
        self.total_recursos_producidos = 0  

    def alimentar(self):
        self.hambre -= 10
        if self.hambre < 0:
            self.hambre = 0
        if self.salud < 90:
            self.salud += 10

    def acariciar(self):
        self.felicidad += 10
        if self.felicidad > 100:
            self.felicidad = 100

        if self.salud < 100:
            self.salud += 10

    def limpieza_y_cuidados(self):
        self.salud += 10
        if self.salud > 100:
            self.salud = 100

    def enfermar(self):
        if self.salud < 50:
            self.salud -= 20
        else:
            self.salud -= 10

    def morir(self):
        return self.salud <= 0 or self.hambre >= 100 or self.felicidad <= 0

    def pasar_dia(self):
        self.hambre += 10
        if self.salud < 50:
            print(f"{self.nombre} está enferm@.")
            self.enfermar()
        else:
            self.salud -= 10
            self.felicidad -= 10

        if self.morir():
            self.salud = 0

    def comprar_animal(self, numero):
        self.nombre = f"{self.nombre} #{numero}"

    def producir(self):
        recursos = random.randint(1, 10)
        self.total_recursos_producidos += recursos  
        return recursos
    

class Vaca(Animal):
    def __init__(self, numero):
        super().__init__("Vaca", salud_max=100, hambre_max=50, felicidad_max=100)
        self.comprar_animal(numero)

    def producir(self):
        return random.randint(5, 10)

class Oveja(Animal):
    def __init__(self, numero):
        super().__init__("Oveja", salud_max=80, hambre_max=40, felicidad_max=90)
        self.comprar_animal(numero)

    def producir(self):
        return random.randint(1, 5)

class Gallina(Animal):
    def __init__(self, numero):
        super().__init__("Gallina", salud_max=60, hambre_max=30, felicidad_max=80)
        self.comprar_animal(numero)

    def producir(self):
        return random.randint(2, 4)

class Granja:
    def __init__(self):
        self.jugador = Jugador()
        self.dinero = 0
        self.creditos = 0
        self.total_recursos_producidos = 0 

    def simular_dia(self):
        print("\nComienza un nuevo día en la granja!")
        self.jugador.cuidar_animales(self)
        for animal in self.jugador.animales:
            recursos = animal.producir()
            animal.total_recursos_producidos += recursos  
            print(f"{animal.nombre} ha producido {recursos} recursos.")

        for animal in self.jugador.animales:
            animal.pasar_dia()
            if animal.morir():
                print(f"{animal.nombre} ha muerto. ¡Cuida bien a los demás!")
                self.jugador.animales.remove(animal)
            elif animal.felicidad <= 0:
                print(f"{animal.nombre} está deprimido. ¡Acarícialo para evitar que muera por depresión!")

        if not self.jugador.animales:
            print("¡Todos tus animales han muerto! Juego terminado.")
            exit()

    def mostrar_dinero_y_creditos(self):
        print(f"Créditos disponibles para comprar animales: {self.creditos} Créditos.")

    def tienda(self):
        while True:
            print("\nBienvenido a la tienda. ¿Qué deseas hacer?")
            print("1. Mostrar recursos producidos por cada animal")
            print("2. Vender recursos")
            print("3. Mostrar dinero y créditos")
            print("4. Comprar animales")
            print("5. Volver a la granja")

            opcion_tienda = input("Elige una opción: ")

            if opcion_tienda == "1":
                self.mostrar_recursos_producidos()
            elif opcion_tienda == "2":
                self.vender_recursos()
            elif opcion_tienda == "3":
                self.mostrar_dinero_y_creditos()
            elif opcion_tienda == "4":
                self.comprar_animales()
            elif opcion_tienda == "5":
                return
            else:
                print("Opción no válida. Por favor, elige una opción válida.")

    def mostrar_recursos_producidos(self):
        print("\nRecursos producidos por cada animal:")
        for animal in self.jugador.animales:
            print(f"{animal.nombre} ha producido {animal.total_recursos_producidos} recursos.")
        print(f"Total de recursos producidos: {sum(animal.total_recursos_producidos for animal in self.jugador.animales)}")

    def vender_recursos(self):
        total_venta = 0
        for animal in self.jugador.animales:
            recursos = animal.total_recursos_producidos 
            if isinstance(animal, Vaca):
                precio_por_recurso = 30
            elif isinstance(animal, Oveja):
                precio_por_recurso = 20
            elif isinstance(animal, Gallina):
                precio_por_recurso = 10
            else:
                precio_por_recurso = 0

            venta_animal = recursos * precio_por_recurso
            total_venta += venta_animal

            print(f"{animal.nombre} ha vendido {recursos} recursos por {venta_animal} Créditos.")

        self.dinero += total_venta
        self.creditos += total_venta


class Jugador:
    def __init__(self):
        self.animales = [Vaca(1), Oveja(1), Gallina(1)]

    def mostrar_menu(self, animal):
        print(f"Acciones disponibles para {animal.nombre}:")
        print("1. Alimentar")
        print("2. Acariciar")
        print("3. Limpieza y Cuidados Médicos")
        print("4. Volver")
        print("5. Ir a la tienda")
        eleccion = input("Elige una opción: ")
        return eleccion

    def cuidar_animales(self, granja):
        while True:
            print("\nAnimales en la granja:")
            for idx, animal in enumerate(self.animales, start=1):
                print(f"{idx}. {animal.nombre} - Salud: {animal.salud}, Hambre: {animal.hambre}, Felicidad: {animal.felicidad}")

            opcion_animal = int(input("\nElige un animal para interactuar (1-3) o 0 para pasar al siguiente día: ")) - 1
            if opcion_animal == -1:
                return

            animal = self.animales[opcion_animal]
            eleccion = self.mostrar_menu(animal)

            if eleccion == "1":
                animal.alimentar()
            elif eleccion == "2":
                animal.acariciar()
            elif eleccion == "3":
                animal.limpieza_y_cuidados()
                animal.salud += 10
                print(f"{animal.nombre} ha recibido cuidados médicos y su salud ha aumentado en 10 puntos.")
            elif eleccion == "4":
                continue
            elif eleccion == "5":
                granja.tienda()
            else:
                print("Opción no válida. Por favor, elige una opción válida.")

            animal.enfermar()
            if animal.morir():
                print(f"{animal.nombre} ha muerto. ¡Cuida bien a los demás!")
                self.animales.remove(animal)

if __name__ == "__main__":
    granja = Granja()

    while True:
        opcion = input("¿Quieres pasar al siguiente día? (s/n): ").lower()
        if opcion == 'n':
            print("Gracias por jugar. ¡Hasta luego!")
            granja.mostrar_dinero_y_creditos()
            break

        granja.simular_dia()
