from statistics import stdev

def ind_unc(d_l, d_f, read):
    lams = diffs(read[1])
    return [0.5 * ((i/100 + d_l) * (read[0] + d_f) - (i/100 - d_l) * (read[0] - d_f)) for i in lams]

def vels(f, reads):
    velocities = []
    for i in range(len(reads) - 1):
        lam = reads[i+1] - reads[i]
        velocities.append(lam/100 * f)
    return velocities

def diffs(arr):
    return [arr[i+1] - arr[i] for i in range(len(arr) - 1)]

def vel(f, reads):
    v_lengths = diffs(reads)
    avg = sum(v_lengths) / len(v_lengths)
    for i in v_lengths:
        if abs(i - avg) > 0.3*avg: #odrzucanie błędów grubych
            v_lengths.remove(i)
    return sum(v_lengths) / len(v_lengths) / 100 * f

def unc(arr):
    return (max(arr) - min(arr))/2

readings = []
input_name = input()
f = open(input_name)
for line in f.readlines():
    line = line.split()
    readings.append((int(line[0]), [float(i) for i in line[1::]]))

velocities = [vel(i[0], i[1]) for i in readings]
v_avg = sum(velocities) / len(velocities)
for i in readings: print(sum(diffs(i[1]))/4)
print("Średnia prędkość dźwięku:", v_avg)
print("Prędkości", velocities)
print("Niepewność pomiaru prędkości dźwięku:", unc(velocities), "m/s")
print("Odchylenie standardowe pomiarów prędkości", stdev(velocities), "m/s")
print('-------------------------------')
print(sum([sum(ind_unc(0.001, i[0] * 0.005 + 1, i))/(len(i[1])-1) for i in readings])/len(readings))
