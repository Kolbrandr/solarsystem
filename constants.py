# Universal Constants
G = 6.674*10**(-20)  # km3⋅kg−1⋅s−2

# Simulation constants
dt = 3600  # time step in seconds
limit = 420000000  # time limit of simulation in seconds

# Gravitational Parameters in km^3/s^2


class GravParameters:
    def __init__(self):
        self.SUN = 1.32712e11
        self.MERCURY = 22032
        self.VENUS = 324859
        self.EARTH = 398600
        self.MOON = 4904.86
        self.MARS = 42828.4
        self.JUPITER = 1.26687e8
        self.SATURN = 3.79311e7
        self.URANUS = 5793940
        self.NEPTUNE = 6836530
        self.PLUTO = 871.9


GravParameters = GravParameters()
