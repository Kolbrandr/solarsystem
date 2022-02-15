import basicFunctions as gen
import constants


sun = gen.Planet("sun", constants.GravParameters.SUN, [0, 0, 0], [0, 0, 0])
jupiter = gen.Planet("jupiter", constants.GravParameters.JUPITER, [8e8, 0, 0], [0, 13, 0])
earth = gen.Planet("earth", constants.GravParameters.EARTH, [1.5e8, 0, 0], [0, 30, 0])


system = [sun, jupiter, earth]
