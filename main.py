import constants
import basicFunctions as fxn
import planets as ss
import matplotlib.pyplot as plt


time = 0  # initialize time

# Iterating the simulation
while time < constants.limit:
    for planet in range(len(ss.system)):
        fxn.calculate_acceleration(ss.system[planet], ss.system)  # finds new acceleration due to all objects in system
        fxn.increment_velocity(ss.system[planet])  # increments velocity for planet
    for planet in range(len(ss.system)):  # once all new velocities are calculated, starts moving objects
        fxn.increment_position(ss.system[planet])  # moves object and appends data
    time += constants.dt

# Visualization
plt.scatter(ss.jupiter.x, ss.jupiter.y, color='orange', marker='.', label='jupiter')
plt.scatter(ss.earth.x, ss.earth.y, color='green', marker='.', label='earth')
plt.legend(loc='upper left')
plt.show()
