import random

people = []

# Ensure the list has an even number of people
if len(people) % 2 != 0:
    raise ValueError("The number of people must be even for proper pairing.")

pairs = []

while people:
    # Randomly select two people from the list and pair them
    person1 = random.choice(people)
    people.remove(person1)
    person2 = random.choice(people)
    people.remove(person2)
    pairs.append((person1, person2))

print(pairs)
