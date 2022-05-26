# Big 0 Notation: Part 2

After working through the first Big O challenge, you should have a pretty good grasp on how to calculate Big O. This next challenge is going to ask you to retroactively calculate the Big O of your previous challenges from weeks 1 and 2.

## Instructions

* As you look through your previous week's challenges (yup, all of them) please note what the Big O complexity is and explain why the complexity is what it is.
* If you come across a solution where you think it could be optimized, please try to implement an optimized version.
 The code below will run each function 500 times and print out the, saving the start and stop times on each run. Then it will print a report with the median run time, mean run time and standard deviation. 

 To use it yourself, just add your function defs and also be sure to add them to the functions variable below the import statements. 

```python
def iterate_a_lot():
  for i in range(1000):
    for j in range(100):
      j

def iterate_a_little():
  for i in range(10):
    i 


# Reporting
import time
import random
import statistics

functions = iterate_a_lot, iterate_a_little

# this is just a one line way to make this: {'iterate_a_lot': [], 'iterate_a_little': []}
times = {f.__name__: [] for f in functions}

for func in functions:
  for i in range(500):  # adjust accordingly so whole thing takes a few sec
    t0 = time.time()
    func()
    t1 = time.time()
    times[func.__name__].append((t1 - t0) * 1000)



for name, numbers in times.items():
  print('FUNCTION:', name, 'Used', len(numbers), 'times')
  print('\tMEDIAN', statistics.median(numbers))
  print('\tMEAN  ', statistics.mean(numbers))
  print('\tSTDEV ', statistics.stdev(numbers))
```
```
FUNCTION: iterate_a_lot Used 500 times
        MEDIAN 2.0799636840820312
        MEAN   2.0910134315490723
        STDEV  0.10131728527084599
FUNCTION: iterate_a_little Used 500 times
        MEDIAN 0.00095367431640625
        MEAN   0.000690460205078125
        STDEV  0.0004778623549334838
```
### Note
This may seem silly, but it is important to remember Big O as you solve problems. A O(N^2) solution is going to cost you later down the road when it could have been solved upfront. Furthermore, for better or worse, interviewers really like these types of questions and it'll be nice to have this for review :smile:
