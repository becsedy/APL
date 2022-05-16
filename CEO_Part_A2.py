import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

def objective(x, a, b, c, d):
    return a * np.cos(b * x + c) * np.e ** (-d * x)

rows = []
data = []
x = []
y = []
with open("CEO Lab Part A Inductor 2.csv", "r", encoding = "utf-8") as infile:
    while True:
        row = infile.readline()
        if row == "":
            break
        else:
            rows.append(row)
            
    for i in range(len(rows)):
        rows[i] = rows[i].split(sep = ",")
        
    for i in range(len(rows)):
        for j in range(3):
            rows[i].pop(0)
        rows[i][0] = float(rows[i][0])
        rows[i][1] = float(rows[i][1].strip())
        
    for i in range(len(rows) - 1, -1, -1):
        if rows[i][0] < 0:
            rows.pop(i)
    
    y_shift = rows[len(rows) - 1][1]
    
    for i in range(len(rows)):
        rows[i][1] -= y_shift
    
    
plt.figure(dpi = 1000)
    
for i in range(len(rows)):
    x.append(rows[i][0])
    y.append(rows[i][1])

popt, _ = curve_fit(objective, x, y)
a, b, c, d = popt
print(a, b, c, d)

x2 = np.arange(0, 0.012, 0.000001)

for i in range(len(x2)):
    plt.plot(x2[i], a * np.cos(b * x2[i] + c) * np.e ** (-d * x2[i]), "o", color = "blue", ms = 0.2)

for i in range(len(rows)):
    plt.plot(rows[i][0], rows[i][1], "o", color = "black", ms = 0.3)
    
plt.show()

'''
y = 34.7 * cos(286000x - 64.8) * e^(-7.40e3 x)
'''