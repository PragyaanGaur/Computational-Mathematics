import random
import matplotlib.pyplot as plt

def pi_(n):
    inside_x, inside_y = [], []
    outside_x, outside_y = [], []
    i = 0

    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 <= 1:
            i += 1
            inside_x.append(x)
            inside_y.append(y)
        else:
            outside_x.append(x)
            outside_y.append(y)

    pi_value = (i / n) * 4

    plt.figure()
    plt.scatter(inside_x, inside_y, s=1)
    plt.scatter(outside_x, outside_y, s=1)
    c = plt.Circle((0, 0), 1, fill=False)
    plt.gca().add_artist(c)
    plt.gca().set_aspect('equal')
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.title(f"Estimate of pi = {pi_value}")
    plt.show()

    return pi_value

print(pi_(20000))
