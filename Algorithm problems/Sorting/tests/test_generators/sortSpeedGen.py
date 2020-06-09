import os 
import numpy as np

os.chdir('Algorithm problems\\Sorting\\tests')

# create huge pool of ints for testing sorting speed

spam = list(np.random.choice(range(-10000000, 10000000), 200000, replace=False))

spam_text = ' '.join(map(str, spam))
fp = open('large_random_ints_unique_2', 'w')

fp.write(spam_text)
fp.close()
print('done')
