import numpy as np
from matplotlib import pyplot as plt

def avg(l):
    for i in range(len(l)):
        l[i] = sum(l[i])/30
    return l

def solve():
    l = [0.50, 0.51] 
    T = [
        [14.179, 14.170, 14.187],
        [14.199, 14.190, 14.198]
    ]
    T = avg(T)   
    g = []
    for i in range(len(l)):
        g.append(4 * ((3.14) ** 2) * l[i] / (T[i] ** 2))
    print(*g)

def solve_reverse():
    
    x = [20, 25, 30, 33.3, 36.6, 40, 45, 50] # [cm]
    Ta = [8,6.04,4,3.5,3.5,4,6.03,8]
    Tb = [9,6,2.5,1.25,1.25,2.5,6,9]
    T = []

    for i in range(len(x)):
        if round(Ta[i],1) == round(Tb[i],1): # round
            T.append(round(Ta[i],2))
    
    Tr = sum(T) / 2
    lr = 0.94 # xb - xa
    # odch stand od sredniej z T1 i T2 to dokladnosc pomiaru czasu
    x_err = (sum([(Ti-Tr)**2 for Ti in T]) / 2)**0.5; print(x_err)
    y_err = 0.5 # [cm]

    mymodel_a = np.poly1d(np.polyfit(x,Ta,5))
    myline_a = np.linspace(min(x),max(x),max(Ta))
    plt.scatter(x, Ta, marker='o', color='blue')
    plt.errorbar(x, Ta, yerr=y_err, xerr=x_err, fmt="o", color='blue')
    plt.plot(myline_a, mymodel_a(myline_a), color='blue')
    mymodel_b = np.poly1d(np.polyfit(x,Tb,5))
    myline_b = np.linspace(min(x),max(x),max(Tb))
    plt.scatter(x,Tb,marker='o', color='red')
    plt.errorbar(x, Tb, yerr=y_err, xerr=x_err, fmt="o", color='red')
    plt.plot(myline_b, mymodel_b(myline_b), color='red')
    plt.xticks(np.arange(int(min(x)), int(max(x))+5, 5))
    plt.yticks(np.arange(0, int(max(Tb))+2, 0.5))
    plt.legend(["Ta", "Tb"])
    plt.show()

if __name__ == "__main__":
    #solve()
    solve_reverse()