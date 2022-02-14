import basicFunctions as gen
import constants


sun = gen.Planet("sun", constants.GravParam.get("sun"), [0, 0, 0], [0, 0, 0])
jupiter = gen.Planet("jupiter", constants.GravParam.get("jupiter"), [8e8, 0, 0], [0, 13, 0])
earth = gen.Planet("earth", constants.GravParam.get("earth"), [1.5e8, 0, 0], [0, 30, 0])

system = [sun, jupiter, earth]
