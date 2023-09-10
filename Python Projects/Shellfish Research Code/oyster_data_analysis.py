import csv
import statistics
import matplotlib.pyplot as plt

f1 = 'oyster_data_bridge.csv'
f2 = 'oyster_data_broad_cove.csv'
f3 = 'oyster_data_little_john_island.csv'

# Base Functions

def list_func(lists, index):
    lst = []
    for i in lists:
        lst.append(i[index])
    
    return lst

def get_x(name):
    with open(name, 'r') as df:
        reader = csv.reader(df)
        x = next(reader)
        df.close()

    return x 
    
def get_body(name):
    with open(name, 'r') as df:
        reader = csv.reader(df)
        data = []
        for row in reader:
            data.append(row)
        df.close()
    
    return data[1:]

def get_y_list(name):
    y = []
    data = get_body(name)
    for i in range(len(data[0])):
        y.append(list_func(data, i))
    
    return y 

# Statistic Functions

def get_stdev(name):
    y_list = get_y_list(name)
    y = []
    for lst in y_list:
        lst = [int(i) for i in lst]
        y.append(round(statistics.stdev(lst), 2))
    
    return y

def med_group(name):
    y_list = get_y_list(name)
    y = []
    for lst in y_list:
        lst = [int(i) for i in lst]
        y.append(round(statistics.median_grouped(lst), 2))
    
    return y

def max_minus_min(name):
    y_list = get_y_list(name)
    y = []
    for lst in y_list:
        lst = [int(i) for i in lst]
        y.append(statistics.median_high(lst) - statistics.median_low(lst))
    
    return y

def max_minus_med(name):
    y_list = get_y_list(name)
    y = []
    for lst in y_list:
        lst = [int(i) for i in lst]
        y.append(round(statistics.median_high(lst) - statistics.median_low(lst), 3))
    
    return y

# Plotting Functions

def plotxy(x, y):
    plt.plot(x, y)
    plt.xlabel('Date')
    plt.ylabel('Standard Deviation')
    plt.title('Oyster Length Standard Deviation Vs. Time')
    plt.show()

def plot_all_stdev():
    plt.plot(x, y1, label='Bridge')
    plt.plot(x, y2, label='Broad Cove')
    plt.plot(x, y3, label='Little John')
    plt.xlabel('Date')
    plt.ylabel('Standard Deviation')
    plt.title('Oyster Length Standard Deviation Vs. Time')
    plt.legend()
    plt.show()

def plot_all_med_size():
    plt.plot(x, y1, label='Bridge')
    plt.plot(x, y2, label='Broad Cove')
    plt.plot(x, y3, label='Little John')
    plt.xlabel('Date')
    plt.ylabel('Size (mm)')
    plt.title('Median Oyster Length Vs. Time')
    plt.legend()
    plt.show()

# Calls 

x = get_x(f1)

"""
y1 = get_stdev(f1)
y2 = get_stdev(f2)
y3 = get_stdev(f3)
plot_all_stdev()

"""

y1 = med_group(f1)
y2 = med_group(f2)
y3 = med_group(f3)
plot_all_med_size()


    


