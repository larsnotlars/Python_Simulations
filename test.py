from this import d
import numpy as np
import matplotlib.pyplot as plt
import random


#function to calculate new state of the nagel schreckenberg model
def new_state(state, n_cars, p):
    tempstate = np.copy(state)
    #step 1
    for i in range(n_cars):
        if state[i] != -1 and state[i] < 5:
            tempstate[i] += 1

    #step 2
    for i in range(n_cars):
        if tempstate[i] != -1:
            j = 1
            while tempstate[(i+j) % n_cars] == -1 and j <= 5:
                j += 1
            if j <= tempstate[i]:
                tempstate[i] = j-1

    #print("temp"+ str(tempstate))

    #step 3
    for i in range(n_cars):
        if random.random() < p and state[i] > 0:
            tempstate[i] -= 1
    #print("third "+str(tempstate))

    #step 4
    newstate = np.full(n_cars, -1)
    for i in range(n_cars):
        if tempstate[i] != -1:
            newstate[(i + tempstate[i]) % n_cars] = tempstate[i]

    #print("fourth "+str(newstate))
    return newstate


n_cars = 100
t = 100
p = 0.3

#create array with 95 numbers 80 times -1 and 15 numbers betweeen 0 and 5
ramdomize = np.concatenate(
    (np.full(80, -1, dtype="int"), np.random.randint(0, 6, 15, dtype="int")))
#shuffle the array
np.random.shuffle(ramdomize)

state = np.concatenate((np.full(5, 0, dtype="int"), ramdomize))

plt.rcParams['image.cmap'] = 'binary'

result = np.zeros((t, n_cars))

result[0] = state

#simulation
for i in range(1, t):
    state = new_state(state, n_cars, p)
    result[i] = state


fig, ax = plt.subplots(figsize=(16, 9))
ax.matshow(result)

#animate the result
def animate(i):
   ax.matshow(result[:i])
   ax.set_title("t = {}".format(i))
   ax.set_xticks([])
   ax.set_yticks([])
   ax.set_xlabel("x")
   ax.set_ylabel("t")
   return ax