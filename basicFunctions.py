import constants
import numpy as np


class Planet:
    def __init__(self, name, mass, position, velocity, acceleration):
        self.name = name  # planet name
        self.mass = mass  # gravitational parameter, in km^3/s^2
        self.position = position  # a vector list, in km
        self.velocity = velocity  # a vector list, in km/s
        self.acceleration = acceleration  # a vector list, in km/s^2
        self.x = []
        self.y = []
        self.z = []

    def display_velocity(self):
        print("Current velocity is " + str(self.velocity) + " km/s")
        # returns planet's velocity

    def display_position(self):
        print("Current position is " + str(self.position)+ " km")
        # returns planet's position

    def display_acceleration(self):
        print("Current position is " + str(self.acceleration)+ " km/s^2")
        # returns planet's acceleration

    def display_mass(self):
        m = str(self.mass/constants.G)
        print("Current mass is " + m + " kg")
        # returns planet's mass


def increment_position(planet):
    for coordinate in range(3):
        planet.position[coordinate] = planet.position[coordinate] + planet.velocity[coordinate]*constants.dt
        # new position = old position + vdt


def increment_velocity(planet):
    for coordinate in range(3):
        planet.velocity[coordinate] = planet.velocity[coordinate] + planet.acceleration[coordinate]*constants.dt
        # new velocity = old velocity + adt


def distance(planet1, planet2):
    del_x = planet1.position[0] - planet2.position[0]
    del_y = planet1.position[1] - planet2.position[1]
    del_z = planet1.position[2] - planet2.position[2]
    dist = (np.power(del_x,2) + del_y**2 + del_z**2)**0.5
    # distance = sqrt(delta x ^2 + ...)
    return dist


def difference(subject, target, coordinate):
    diff = target.position[coordinate] - subject.position[coordinate]
    # gives a distance **vector** between objects
    return diff


def calculate_acceleration(planet, system):
    a_x = 0
    a_y = 0
    a_z = 0
    for subject in range(len(system)):  # iterates through all objects in system
        body = system[subject]  # a body pulling on the current object
        if planet.name != body.name:  # excludes self from calculation
            a_x += ((body.mass * difference(planet, body, 0)/10**6) / np.power(distance(planet, body)/10**6, 3))/10**12
            a_y += ((body.mass * difference(planet, body, 1)/10**6) / np.power(distance(planet, body)/10**6, 3))/10**12
            a_z += ((body.mass * difference(planet, body, 2)/10**6) / np.power(distance(planet, body)/10**6, 3))/10**12
    planet.acceleration = [a_x, a_y, a_z]  # sets acceleration within planet object


