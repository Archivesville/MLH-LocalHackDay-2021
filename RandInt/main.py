from time import time

def time_random():
 return time() - float(str(time()).split('.')[0])

def randint(min, max):
 return int(time_random() * (max - min) + min)

print(randint(1, 100))