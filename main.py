from statistics import mean
import matplotlib.pyplot as plt
import numpy as np

independent = input("What is your independent variable?\nindependent(unit):  ")
dependent = input("What is your dependent variable?\ndependent(unit): ")
intervals = [int(x) for x in input(f"\nWhich {independent} values are you measuring? \nPlease seperate your answers with commas.: ").split(', ')]

try:
    intervals[0]
except IndexError:
    raise IndexError(f"PLease enter at least 5 {independent} values") from None

results1 = [int(x) for x in input(f"What are the results of {intervals[0]}: ").split(', ')]

try:
    intervals[1]
except IndexError:
    raise IndexError(f"PLease enter at least 5 {independent} values") from None

results2 = [int(x) for x in input(f"What are the results of {intervals[1]}: ").split(', ')]

try:
    intervals[2]
except IndexError:
    raise IndexError(f"PLease enter at least 5 {independent} values") from None

results3 = [int(x) for x in input(f"What are the results of {intervals[2]}: ").split(', ')]

try:
    intervals[3]
except IndexError:
    raise IndexError(f"PLease enter at least 5 {independent} values") from None

results4 = [int(x) for x in input(f"What are the results of {intervals[3]}: ").split(', ')]

try:
    intervals[4]
except IndexError:
    raise IndexError(f"PLease enter at least 5 {independent} values") from None

results5 = [int(x) for x in input(f"What are the results of {intervals[4]}: ").split(', ')]

# processing data
def average(a):
    return mean(a)

def range(list):
    list.sort()
    min = list[0]
    max = list[-1]
    return max - min


print(f"\nThe average of {intervals[0]} is {average(results1)}. The Range is {range(results1)}")
print(f"\nThe average of {intervals[1]} is {average(results2)}. The Range is {range(results2)}")
print(f"\nThe average of {intervals[2]} is {average(results3)}. The Range is {range(results3)}")
print(f"\nThe average of {intervals[3]} is {average(results4)}. The Range is {range(results4)}")
print(f"\nThe average of {intervals[4]} is {average(results5)}. The Range is {range(results5)}")

# graphing

y = np.array(intervals)
x = np.array([average(results1), average(results2), average(results3), average(results4), average(results5)])
xerrorbars = [range(results1) / 2, range(results2) / 2, range(results3) / 2, range(results4) / 2, range(results5) / 2]

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
