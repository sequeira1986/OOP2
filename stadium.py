
class Stadium:
    def __init__(self, stadium_name, date_of_opening, country, city, seat_capacity):
        self.nombre = stadium_name
        self.edad = date_of_opening
        self.estado = country
        self.ciudad = city
        self.asientos = seat_capacity
    def __str__(self):
        return self.nombre + " " + str(self.asientos)
# Create a new stadium object
stadium = Stadium("Estadio Azteca", "29-11-1981", "Mexico", "Mexico City", 87000)
stadium1 = Stadium("Estadio Pepe", "29-11-1981", "Mexico", "Mexico City", 7000)
stadium2 = Stadium("Estadio Lolo", "29-11-1981", "Mexico", "Mexico City", 88000)
stadium3 = Stadium("Estadio Mama", "29-11-1981", "Mexico", "Mexico City", 67000)
stadium4 = Stadium("Estadio Perro", "29-11-1981", "Mexico", "Mexico City", 77000)
stadium5 = Stadium("Estadio Azteca", "29-11-1981", "Mexico", "Mexico City", 97000)
stadium6 = Stadium("Estadio Tiburones", "29-11-1981", "Mexico", "Mexico City", 108000)

stadia = [stadium, stadium1, stadium2, stadium3, stadium4,stadium5, stadium6]
stadia.sort(key=lambda i: i.asientos, reverse=True)

print(stadia[0].nombre)
print(stadia[0].nombre,"es el mas grande tiene una capacidad de",stadia[0].asientos, "asientos,")
print("fue abierto ", stadia[0].edad)
print(stadium)


