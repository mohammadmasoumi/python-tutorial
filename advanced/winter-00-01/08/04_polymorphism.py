
class Parrot:

    def __init__(self) -> None:
        print("Parrot is ready")

    def fly(self):
        print("Parrot is flying.")

    def eat(self):
        print("Parrot is eating.")

    def sing(self, song):
        print(f"Parrot is singing {song}")


class Panguin:

    def __init__(self) -> None:
        print("Panguin is ready")

    def fly(self):
        print("Panguin can not fly.")

    def eat(self):
        print("Panguin is eating.")

    def sing(self, song):
        print(f"Panguin is singing {song}")


def test_fly(bird):
    bird.fly()


peggy = Panguin()
tiny = Parrot()
asghar = Parrot()

test_fly(peggy)
test_fly(tiny)

birds = [peggy, tiny, asghar]

for bird in birds:
    bird.fly()

