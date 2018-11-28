import numpy as np

people = []

y = np.random.choice(people, len(people)//2, replace=False)

people_prime = list(set(people) - set(y))

print (list(zip(people_prime, y)))
