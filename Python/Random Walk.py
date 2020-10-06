"" Conducting some tests on my own ""


import numpy as np
import matplotlib.pyplot as plt

np.random.seed()
all_walk = []
for i in range(10):
    complete_walk = [0]
    for x in range(100):
        step = complete_walk [-1]
        dice=np.random.randint(1,7)
        if dice <= 2:
            step = max (0, step -1)
        elif dice > 2 and dice <= 5:
            step = step + 1
        else:
            extra_step = np.random.randint (1,7)
            step = step + extra_step
        complete_walk.append(step)
    all_walk.append(complete_walk)
print (all_walk)
all_walk_t = np.transpose(all_walk)
plt.plot(all_walk_t)
plt.show()
plt.clf()
plt.hist(all_walk, bins = 10)
plt.show()


# In[ ]:




