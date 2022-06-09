# Big O

used to describe relative performance of an algorithm
- not concerned with specific time an algo takes, or space it takes up
- we are concerned with how the algorithm takes more time as the input size grows (time complexity), or memory usage grows as input size grows (space complexity)
- generally when talking about complexity analysis, we're more concerned with time complexity than space complexity

problems that we analyze with big-o are generally going to take an array as input. 

assumptions for big-o analysis:
- we're only concerned with the worst-case scenario
- it is assumed that all operations take the same amount of time, so this is roughly equal to measuring time
- only the largest term matters.  
    - 3n^2 + 4n + 1000 -> O(n^2)
    - n + n -> n


