# The Kelly Criterion

import random
import time
import matplotlib.pyplot as plt

def invest(win_factor, loss_factor, money, chance_results, fraction_invested):
     for result in chance_results:
          if result == 1:
               money = money * ((1 - fraction_invested) + (fraction_invested * win_factor))
          if result == 0:
               money = money * ((1 - fraction_invested) + (fraction_invested * loss_factor))
     
     return money

def cycle(win_factor, loss_factor, money, chance_results):
     x = 0 
     invest_results_orig = []
     invest_results = []
     while x <= 1.025:
          invest_results_orig.append(invest(win_factor, loss_factor, money, chance_results, x))
          x += 0.025
     
     for i in invest_results_orig:
          invest_results.append(round(i, 2))

     return invest_results

def graph_cycle(win_factor, loss_factor, money, chance_results):
     x = []
     y = []
     data_list = list(enumerate(cycle(win_factor, loss_factor, money, chance_results)))
     for i in data_list:
          x.append(i[0] * 2.5), y.append(i[1])
     
     plt.plot(x,y)
     plt.show()

def get_ncr(number_flips):
     new_chance_res = []
     for i in range(number_flips):
          new_chance_res.append(random.randint(0,1))
     
     return new_chance_res

def find_optimal(win_factor, loss_factor, money, number_flips):
     max_list =  []
     for i in range(2 ** number_flips):
          cycle_res = cycle(win_factor, loss_factor, money, get_ncr(number_flips))
          max_list.append(cycle_res.index(max(cycle_res)))
     
     return sum(max_list) / len(max_list) * 2.5

def invest_once(win_factor, loss_factor, money, result, fraction_invested):
     if result == 1:
               money = money * ((1 - fraction_invested) + (fraction_invested * win_factor))
     if result == 0:
          money = money * ((1 - fraction_invested) + (fraction_invested * loss_factor))
     
     return money     

def graph_optimal(win_factor, loss_factor, money, number_flips):
     frac_inv = find_optimal(win_factor, loss_factor, money, number_flips) / 100
     x = list(range(0, number_flips + 1))
     y = [100]
     
     count = len(x) - 1
     z = 0
     inv_money = money
     while z < count:
          inv_money = invest_once(win_factor, loss_factor, inv_money, random.randint(0,1), frac_inv)
          y.append(inv_money)
          z += 1

     plt.title('Value vs. Time')
     plt.xlabel('Time (# Flips)')
     plt.ylabel('Value')
     plt.plot(x,y)
     plt.show()

print(find_optimal(2, 0, 100, 10))
graph_optimal(2, 0, 100, 10)





