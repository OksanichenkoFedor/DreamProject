from LevelParts.Units.Unit import *

def Ch(a):
    a.life = 1
    print(a.life)

def CCC(a):
    Ch(a)


A = Unit(["union","left"],10,[0,0,0],0,0,0,0)
print(A.life)
CCC(A)
print(A.life)
