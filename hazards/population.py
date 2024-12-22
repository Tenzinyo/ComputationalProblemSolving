#Write a function growth1(totalDays) that simulates a population growing by 3 individuals each day. For each day, print the day number and the total population size.
#Also plot the graph to analyze the growth

import matplotlib.pyplot as pyplot
def totalDays(initial_population,days):
    population=initial_population
    populationList= []
    populationList.append(initial_population)
    pop_list=[]
    days_list=[]
    for days in range(1, days+1):
        total_population= 3*population * days
        pop_list.append(total_population)
        days_list.append(days)
        print(total_population,days)
    pyplot.plot(days_list, pop_list)
    return total_population
def main():
    total_population=totalDays(1000,120)
    print('The final population is ' +  str(total_population) + '.')
main()
        

#Write a function growth2(totalDays) that simulates a population that grows by 3
# individuals each day but also shrinks by, on average, 1 individual every 2 days. 
 #For each day, print the day number and the total population size.
#Also plot the graph to analyze the growth.

import matplotlib.pyplot as pyplot
def totalDays(initial_population,days):
    population=initial_population
    populationList= []
    populationList.append(initial_population)
    pop_list=[]
    days_list=[]
    for days in range(1, days+1):
        total_population= 3*population * 1-(2*days)
        pop_list.append(total_population)
        days_list.append(days)
        print(total_population,days)
    pyplot.plot(days_list, pop_list)
    return total_population
def main():
    total_population=totalDays(1000,120)
    print('The final population is ' +  str(total_population) + '.')
main()

#Modify growth2(population), to return the number f years it will take to increase the population ten times 
#of initial population.
import math
import matplotlib.pyplot as pyplot
def totalDays(initial_population,days):
    population=initial_population
    populationList= []
    populationList.append(initial_population)
    pop_list=[]
    days_list=[]
    total_population= initial_population
    days=1
    while total_population < 100* initial_population:
        #print('days= '+ str(days))
        days= days+1
        total_population= 3*total_population * days
        pop_list.append(total_population)
        days_list.append(days)
        print(total_population,days)
    pyplot.plot(days_list, pop_list)
    return total_population
def main():
    total_population=totalDays(1000,120)
   # print('The final population is '  +  str(total_population) + ' and it takes ' + str(number_of_days)+ ' days for the population to grow by ten times of the initial population ')
main()








