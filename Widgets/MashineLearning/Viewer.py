import matplotlib.pyplot as plt
import numpy as np
number = 800
file_obj = open("differentAI/results1.txt", "r")
union = []
order = []

def ret_union(n):
    return Union[n]

def ret_order(n):
    return Order[n]

for i in range(number):
    union.append(min(float(file_obj.readline()), 1500000.0))
    order.append(float(file_obj.readline()))
Union = np.array(union)
Order = np.array(order)

Numbers = np.arange(number)

plt.plot(Numbers, Union, '-', Numbers, Order, '-')
plt.show()
print(union)