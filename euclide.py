import sys
import math
import time 
from datetime import timedelta

#Cacule du PGCD
def pgcd(dividende, diviser) :
    quotien = sys.maxsize
    while (quotien != 0):
        tab = euclide(dividende, diviser)
        dividende = tab[2]
        diviser = tab[0]
        quotien = tab[3]

        if(tab[0] == 1):
            return tab[0]
            break

    return tab[0]

 
#Calcule de quotien et le reste, Méthode euclidienne
def euclide(dividende, diviser):
    quotient = 0
    reste = dividende
    
    while reste > diviser:
        reste = reste - diviser
        quotient+=1 
        
    return [reste, dividende, diviser, quotient]

#Calcule de bezout
def bezout(a,b):
    r, u, v = a, 1, 0
    rp, up, vp = b, 0, 1
    while rp != 0:
        q = r//rp
        rs, us, vs = r, u, v
        r, u, v = rp, up, vp
        rp, up, vp = (rs - q*rp), (us - q*up), (vs - q*vp)
    print('u = ',v)
    print('v = ',u)

def main(argv):
    #Message d'accueil
    print("\n####################################### \n|BIENVENUE DANS LE PROGRAMME D'EUCLIDE| \n#######################################")

    #Déclarations des variables
    try:
        dividende = int(input('\nEntrer le dividende: '))
        diviser = int(input('Entrer le diviser: '))
    except ValueError:
        print("\nCe nombre n'est pas valide. Arrêt du programme... ")
        sys.exit(1)

    if(pgcd(dividende, diviser) == 1):
        print('premier entre eux')
        bezout(dividende, diviser)
    else:
        print('nope')

if __name__ == '__main__':
    main(sys.argv)