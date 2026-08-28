import random

random_number1 = random.randint(0, 9)
random_number2 = random.randint(0, 9)
random_number3 = random.randint(0, 9)

random_number4 = random.randint(1, 6)
random_number5 = random.randint(1, 6)
random_number6 = random.randint(1, 6)
random_number7 = random.randint(1, 6)

kolmenumeroinen_koodi = str(random_number1) + str(random_number2) + str(random_number3)
nelinumeroinen_koodi = str(random_number4) + str(random_number5) + str(random_number6) + str(random_number7)

print("Kolmenumeroinen koodi = " + kolmenumeroinen_koodi)
print("Nelinumeroinen koodi = " + nelinumeroinen_koodi)