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
    for planet in range(len(ss.system)):  # once all new velocities are calculated, starts moving object
        fxn.increment_position(ss.system[planet])  # moves object and appends data
    time += constants.dt


# Visualization
fig = plt.figure()
fig.set_size_inches(5, 5)
ax = fig.add_subplot(111)
ax.set_aspect('equal')
ax.plot(ss.jupiter.x, ss.jupiter.y, color='orange', label='jupiter')
ax.plot(ss.earth.x, ss.earth.y, color='green', label='earth')
ax.plot(ss.moon.x, ss.moon.y, color='gray', label='moon')
plt.legend(loc='upper left')
plt.xlabel('km')
plt.ylabel('km')
plt.show()
