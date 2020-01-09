import matplotlib.pyplot as plt
from random import randint

class RandomWalk:

    def __init__(self):
        self.x_values = [0]
        self.y_values = [0]

    def walk(self):
        while abs(self.x_values[-1])<500:
            new_x_value = randint(-5,5)
            new_y_value = randint(-5,5)
            if new_x_value != 0 or new_y_value!=0:
                self.x_values.append(self.x_values[-1]+new_x_value)
                self.y_values.append(self.y_values[-1]+new_y_value)

while True:
    rw = RandomWalk()
    rw.walk()

    x_values = rw.x_values
    y_values = rw.y_values

    fig, ax = plt.subplots(figsize=(15,9))
    ax.set_title('Random walking...', fontsize=24)
    ax.set_xlabel('position x', fontsize=14)
    ax.set_ylabel('position y', fontsize=14)
    ax.tick_params(axis='both',labelsize=14)
    num_steps = list(range(0,len(x_values)))
    ax.scatter(x_values, y_values, c=num_steps,cmap=plt.cm.Blues, s=1)
    ax.scatter(x_values[0], y_values[0], c='green', s=20)
    ax.scatter(x_values[-1], y_values[-1], c='red', s=20)

    plt.show()

    stop = input('press q to quit, any other key to continue: ')
    if stop == 'q':
        break
        
