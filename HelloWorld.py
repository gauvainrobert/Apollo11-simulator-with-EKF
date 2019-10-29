#! /usr/bin/python3
import ephem
import datetime
import math

#documentation PyEphem: https://rhodesmill.org/pyephem/quick.html#
#on peut verifier les calculs ici: https://www.suncalc.org/

home = ephem.Observer()
home.lat, home.lon = 43.60072, 1.43289 #coordonees de Toulouse
home.date = datetime.date(1990,4,19) #time.utcnow() #la date d' aujourd'hui

sun = ephem.Sun()
sun.compute(home)
print ("RA = ", sun.ra, " | Dec = ", sun.dec)

r = 1.004323

x = r*math.cos(sun.ra)*math.cos(sun.dec)
y = r*math.sin(sun.ra)*math.cos(sun.dec)
z = r*math.sin(sun.dec)

print ("X:", x, " Y:", y, " Z:", z)
