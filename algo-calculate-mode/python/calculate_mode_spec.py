# Write your own unit tests here!
from calculate_mode import calculate_mode

tests = [
    {'test':[1,2,3,3],                          'ans':[3]},
    {'test':[4.5, 0, 0],                        'ans':[0]},
    {'test':[1.5, -1, 1, 1.5],                  'ans':[1.5]},
    {'test':[1,1,2,2],                          'ans':[1,2]},
    {'test':[1,2,3],                            'ans':[1,2,3]},
    {'test':["who", "what", "where", "who"],    'ans':['who']},
]

tested_function = calculate_mode
count = 0
total = len(tests)

for i in range(total):
    if(tested_function(tests[i]['test']) == tests[i]['ans']):
        print(f'Passed test {i+1} of {len(tests)}')
        count += 1
    else:
        print(f'Failed test {i+1} of {len(tests)}')

print(f'{count}/{total} tests passed.')