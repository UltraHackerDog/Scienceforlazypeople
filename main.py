from statistics import mean
import matplotlib.pyplot as plt
import numpy as np

independent = input("What is your independent variable?\nindependent(unit):  ")
dependent = input("What is your dependent variable?\ndependent(unit): ")
intervals = [int(x) for x in input(f"\nWhich {independent} values are you measuring? \nPlease seperate your answers with commas.: ").split(',')]

results = []
for interval in intervals:
    results.append([int(x) for x in input(f"What are the results of {interval}: ").split(',')])

# processing data
def valrange(list):
    list.sort()
    min = list[0]
    max = list[-1]
    return max - min


for result in results:
    print(f"The average of {result} is {mean(result)} and the range is {valrange(result)}")
    print("-" * 50)

# graphing

y = np.array([mean(result) for result in results])
x = np.array(intervals)
xerrorbars = [valrange(result) / 2 for result in results]

def give_me_a_straight_line(x,y):
    w, b  = np.polyfit(x,y,deg=1)
    line  = w * x + b
    return line

line = give_me_a_straight_line(x,y)

plt.plot(x,y,'o')
plt.plot(x,line,'r--')

plt.errorbar(x, y, xerr=xerrorbars, fmt="o", color="blue")
plt.ylabel(independent)
plt.xlabel(dependent)
plt.grid()
plt.show()
