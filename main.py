import random
import math
import matplotlib.pyplot as plt

x_vals_max = list()
y_vals_max = list()
x_vals_root = list()
y_vals_root = list()

for x in range(5000):
    n1_max = random.random()
    n2_max = random.random()
    x_vals_max.append(max(n1_max, n2_max))
    x_vals_max.sort()

    n_root = random.random()
    n_root = math.sqrt(n_root)
    x_vals_root.append(n_root)
    x_vals_root.sort()

for value in x_vals_max:
    if math.floor(value * 100) < 9:
        x_vals_max.remove(value)
    else:
        x_vals_max[x_vals_max.index(value)] = math.floor(value * 10)

for value in x_vals_max:
    if value == 0:
        x_vals_max.remove(value)

x_vals_max.sort()

x_vals_max_remove = list()

for value in x_vals_max:
    if value < 1:
        x_vals_max_remove.append(value)
        x_vals_max.sort()
    elif value >= 1:
        break

for value in x_vals_max_remove:
    x_vals_max.remove(value)

x_vals_max.sort()

y_vals_max = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for value in x_vals_max:
    match value:
        case 1:
            y_vals_max[0] += 1
        case 2:
            y_vals_max[1] += 1
        case 3:
            y_vals_max[2] += 1
        case 4:
            y_vals_max[3] += 1
        case 5:
            y_vals_max[4] += 1
        case 6:
            y_vals_max[5] += 1
        case 7:
            y_vals_max[6] += 1
        case 8:
            y_vals_max[7] += 1
        case 9:
            y_vals_max[8] += 1

x_vals_root_remove = list()

for i, value in enumerate(x_vals_root):
    x_vals_root[i] = math.floor(value * 10)

x_vals_root.sort()

for value in x_vals_root:
    if value < 1:
        x_vals_root_remove.append(value)

for value in x_vals_root_remove:
    x_vals_root.remove(value)

x_vals_root.sort()

y_vals_root = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for value in x_vals_root:
    match value:
        case 1:
            y_vals_root[0] += 1
        case 2:
            y_vals_root[1] += 1
        case 3:
            y_vals_root[2] += 1
        case 4:
            y_vals_root[3] += 1
        case 5:
            y_vals_root[4] += 1
        case 6:
            y_vals_root[5] += 1
        case 7:
            y_vals_root[6] += 1
        case 8:
            y_vals_root[7] += 1
        case 9:
            y_vals_root[8] += 1

x_vals_max = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x_vals_root = [1, 2, 3, 4, 5, 6, 7, 8, 9]

plt.xlim(1, 9)
plt.ylim(1, 9)

plt.subplot(121).set_title("Max")
plt.plot(x_vals_max, y_vals_max)

plt.subplot(122).set_title("Root")
plt.plot(x_vals_root, y_vals_root)

plt.show()
