import os
from statistics import stdev

def lens(O, P):
    return [i[0]*i[1]/(i[0]+i[1]) for i in zip(O, P)]

def bessel(O, P, L):
    e = [i[0] - i[1] for i in zip(O, P)]
    return [(i[0]**2 - i[1]**2)/(4*i[0]) for i in zip(L, e)]

for file in os.listdir("readings_302"):
    f = open("readings_302/{}".format(file), 'r')
    print(file)
    r_o = []
    r_p = []
    r_l = []
    for line in f.readlines():
        line = line.split()
        r_o.append(float(line[0]) / 100)
        r_p.append(float(line[1]) / 100)
        r_l.append(float(line[2]) / 100)
    print("pierwsza metoda:")
    ans = lens(r_o, r_p)
    print("Średnia ogniskowa:", sum(ans)/len(ans))
    print("Odchylenie standardowe:", stdev(ans))
    print("Niepewność pomiarowa:", (max(ans) - min(ans))/2)
    print("druga metoda:")
    ans = bessel(r_o, r_p, r_l)
    print("Średnia ogniskowa:", sum(ans)/len(ans))
    print("Odchylenie standardowe:", stdev(ans))
    print("Niepewność pomiarowa:", (max(ans) - min(ans))/2)
    f.close()
