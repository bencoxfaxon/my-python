#Importing Data in Real Time

import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


x_vals = []
y_vals = []

index = count()

def animate(i):
    data = pd.read_csv('data.csv')
    x = data['x']
    y1 = data['total_1']
    y2 = data['total_2']
    plt.cla()
    plt.plot(x, y1, label='Random 1')
    plt.plot(x, y2, label='Random 2')
    plt.legend(loc='upper left')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()


"""
x = [1, 2, 3, 4, 5, 6]
y = [1, 3, 8, 15, 24, 35]
plt.title('Test Graph')
plt.ylabel('Test Y')
plt.xlabel('Test X')

plt.plot(x, y, color ='#5a7d9a', linestyle = '--', marker = 'o', linewidth = 2, label = 'test')
plt.legend()
plt.show()
"""
