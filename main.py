# Science solver code made by UltraHackerDog on github.
from statistics import mean



independent = input("What is your independent variable?: ")
intervals = [int(x) for x in input(f"\nWhich {independent} are you measuring? \nPlease seperate your answers with commas.: ").split(', ')]
results1 = [int(x) for x in input(f"What are the results of {intervals[0]}: ").split(', ')]
results2 = [int(x) for x in input(f"What are the results of {intervals[1]}: ").split(', ')]
results3 = [int(x) for x in input(f"What are the results of {intervals[2]}: ").split(', ')]
results4 = [int(x) for x in input(f"What are the results of {intervals[3]}: ").split(', ')]
results5 = [int(x) for x in input(f"What are the results of {intervals[4]}: ").split(', ')]
# processing data
def average(a):
    return mean(a)

def range(list):
    list.sort()
    min = list[0]
    max = list[-1]
    return max - min


print(f"The average of {intervals[0]} is {average(results1)}\nThe Range is {range(results1)}")
print(f"The average of {intervals[1]} is {average(results2)}\nThe Range is {range(results2)}")
print(f"The average of {intervals[2]} is {average(results3)}\nThe Range is {range(results3)}")
print(f"The average of {intervals[3]} is {average(results4)}\nThe Range is {range(results4)}")
print(f"The average of {intervals[4]} is {average(results5)}\nThe Range is {range(results5)}")
