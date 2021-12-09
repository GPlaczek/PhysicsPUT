import os

VOLTAGE = 78.5 # Na początku było 78.3, trochę to wzrastało podczas pomiarów

def k(C, R, T):
    # T = C R K
    return T / (C * R)

def c(k, R, T):
    return T / (R * k)

def T(t, n): return t / n

readings = []

f = open("zad201.in", "r")
for line in f.readlines():
    line = line.split()
    readings.append((float(line[0]), float(line[1]), float(line[2]), int(line[3])))
for i in readings:
    print(k(i[0], i[1], T(i[2], i[3])))

avg = sum(k(i[0], i[1], T(i[2], i[3])) for i in readings) / len(readings)
print('---------------------------------')
print(avg)
print('---------------------------------')
f.close()
for r in os.listdir("readings_201"):
    f = open("readings_201/" + r)
    readings_c = []
    for line in f.readlines():
        line = line.split()
        readings_c.append((float(line[0]), float(line[1]), int(line[2])))

    for i in readings_c:
        print(c(avg, i[0], T(i[1], i[2])))
    f.close()
    print('--------------------------')
