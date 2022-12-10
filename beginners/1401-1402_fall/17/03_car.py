
class Tire:

    def __init__(self, color, ring, thickness, height, cost):
        self.color = color
        self.ring = ring
        self.thickness = thickness
        self.height = height
        self.cost = cost

    def __str__(self):
        # cast -> str
        return f"{self.color}-{self.cost}"

# a = int(22)
# b = 22


class Glass:

    def __init__(self, opacity, bullet_proof, color, material):
        self.opacity = opacity
        self.bullet_proof = bullet_proof
        self.color = color
        self.material = material

    def __str__(self):
        return f"{self.opacity}-{self.color}"


class Car:

    def __init__(self, tire, glass):
        # Composition
        self.tire = tire
        self.glass = glass

    def __str__(self):
        return f"tire: {self.tire} | glass: {self.glass}"


tire1 = Tire(
    color="black", ring="Almi", thickness="22mm", height="50cm", cost=5500
)
tire2 = Tire(
    color="white", ring="Gold", thickness="22mm", height="50cm", cost=5500000
)

glass1 = Glass(
    opacity=10, bullet_proof=True, color="smoky", material="marghoob")
glass2 = Glass(
    opacity=50, bullet_proof=False, color="tranparent", material="bonjool"
)

car1 = Car(tire=tire1, glass=glass2)
car2 = Car(tire=tire2, glass=glass2)

# cast to str
print(car1)
print(car1.tire)
print(car2.tire)
