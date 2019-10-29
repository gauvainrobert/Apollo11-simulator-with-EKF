import ephem
import datetime
import math
import numpy as np
pi = 3.14159265359
def calcul_date(jour,mois,annee):
    #Format a utiliser : jour : 1-31, mois : 1-12, annee : 2000
    date = 367*annee -(7*(annee+((mois+9)/12)))/4+(275*mois)/9+jour-730530
    return date

def rev(x):
    #Remettre x entre 0 et 360 degre
    rev=x-math.trunc((x/360.0))*360.0
    if rev<0.0:
        rev+=360.0
    return rev

def calcul_position_soleil (date):
    #Calcul en x, y, z de la position du Soleil
    w = 282.9404+4.70935e-5*date #longitude du perihelion
    a = 1.0 #distance moyenne
    e = 0.016709-1.151e-9*date # eccentricity
    M = rev(356.047+0.9856002585*date) #anomalie moyenne
    oblecl = 23.4393-3.563e-7*date #obliquite ecliptique
    L = w+M #longitude moyenne du Soleil
    if L>360.0:
        L -=360.0

    E = M+(180/pi)*e*np.sin(np.deg2rad(M))*(1+e*np.cos(np.deg2rad(M)))
    print "\ndate = ", date
    print "w = ", w
    print "a = ", a
    print "e = ", e
    print "M = ", M
    print "oblecl = ", oblecl
    print "L = ", L
    print "E = ", E
    print "cos(90) = ", np.rad2deg(np.cos(0)), "\n"


    #coordonnees rectangulaire dans le plan elliptique
    x_eclip = np.cos(np.deg2rad(E))-e
    y_eclip = np.sin(np.deg2rad(E))*np.sqrt(1-e*e)

    r = np.sqrt(x_eclip*x_eclip + y_eclip*y_eclip)
    v = np.rad2deg(math.atan2(y_eclip,x_eclip))

    lon = v+w

    print "x_eclip = ", x_eclip
    print "y_eclip = ", y_eclip
    print "r = ", r
    print "v = ", v
    print "lon = ", lon

    x2 = r*np.cos(np.deg2rad(lon))
    y2 = r*np.sin(np.deg2rad(lon))
    z2 = 0.0

    print "x2 = ", x2
    print "y2 = ", y2
    #coordonnees equatoriales
    x_equat = x2
    y_equat = y2*np.cos(np.deg2rad(oblecl))-z2*np.sin(np.deg2rad(oblecl))
    z_equat = y2*np.sin(np.deg2rad(oblecl))-z2*np.cos(np.deg2rad(oblecl))
    print "\nx = ", x_equat, "y = ", y_equat, "z = ", z_equat,"\n"


calcul_position_soleil(calcul_date(19,4,1990))
