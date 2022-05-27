from pickle import APPEND

def fibonacci(n):
  solutions = []
  for x in range(n+1):
    if x == 0:
      solutions.append(0)
    elif x == 1:
      solutions.append(1)
    else:
      solutions.append(solutions[x-1] + solutions[x-2])
  return solutions.pop()

fibonacci(10)