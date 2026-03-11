class Ship:
    def __init__(self):
        self.has_paluba = True

    def get_size(self):
        return None

class Podlodka(Ship):
    def __init__(self):
        super().__init__()
        self.size = "25m2"

    def get_size(self):
        return self.size

class Barzha(Ship):
    def __init__(self):
        super().__init__()
        self.size = "100m2"

    def get_size(self):
        return self.size


def get_ship_size(ship: Ship):
    print(ship.get_size())

barzha = Barzha ()
podlodka = Podlodka ()

get_ship_size(podlodka)