
from traceback import print_tb



def grav1(G,M_earth,M_particle,R_earth,y,g):
    return (-G*((M_earth*M_particle)/( R_earth + y)**2))


def grav2(G, M_earth, M_particle, R_earth, y, g):
    return (M_particle*g)

def abc(func):
    return func(1,1,1,1,1,1)

print(abc(grav1))