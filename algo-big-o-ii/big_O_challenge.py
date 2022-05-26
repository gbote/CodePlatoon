# Explain, optimize, and benchmark your python code here.
# Read the README.md file! It requires you to look back through past challenges and note what each algorithm's Big O
# complexity is and why so. It also asks you optimize some of the challenges as well.

# Use this code below to calculate statistics on the challenges' run times.
def iterate_a_lot():
  for _, j in itertools.product(range(1000), range(100)):
      j

def iterate_a_little():
  for i in range(10):
    i 


# Reporting
import itertools
import time
import random
import statistics

functions = iterate_a_lot, iterate_a_little

# this is just a one line way to make this: {'iterate_a_lot': [], 'iterate_a_little': []}
times = {f.__name__: [] for f in functions}

for func, _ in itertools.product(functions, range(500)):
  t0 = time.time()
  func()
  t1 = time.time()
  times[func.__name__].append((t1 - t0) * 1000)



for name, numbers in times.items():
  print('FUNCTION:', name, 'Used', len(numbers), 'times')
  print('\tMEDIAN', statistics.median(numbers))
  print('\tMEAN  ', statistics.mean(numbers))
  print('\tSTDEV ', statistics.stdev(numbers))