
class Car:
    # model, produced_date, speed: param
    def __init__(self, model, produced_date, speed):
        # properties
        #   - model
        #   - produced_date
        #   - speed
        #   - country

        # self: current instance

        # self.property = value of property
        #   property
        self.model = model  # param
        self.produced_date = produced_date
        self.speed = speed
        self.country = "Iran"  # we don't need to get the value of each property from input


# "peraido", "1400", 160 argument
peraido = Car("peraido", "1400", 160)  # instance
peju = Car("peju", "1402", 200)  # instance
