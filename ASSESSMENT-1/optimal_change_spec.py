from optimal_change import optimal_change

tests = [
    {'in1': 62.13,  'in2': 100,  'ans':"The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies."},
    {'in1': 62.13,  'in2': 0,  'ans':"Sorry, you didn't pay enough. You must pay $62.13 to buy this item"},
    {'in1': 62.13,  'in2': .01,  'ans':"Sorry, you didn't pay enough. You must pay $62.12 to buy this item"},
    {'in1': 62.13,  'in2': 1,  'ans':"Sorry, you didn't pay enough. You must pay $61.13 to buy this item"},
    {'in1': 62.13,  'in2': 599.99,  'ans':"The optimal change for an item that costs $62.13 with an amount paid of $599.99 is 5 $100 bills, 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 1 penny."},
    {'in1': 19.25,  'in2': 156.89,  'ans':"The optimal change for an item that costs $19.25 with an amount paid of $156.89 is 1 $100 bill, 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 2 quarters, 1 dime, and 4 pennies."},
    {'in1': 0,  'in2': 89.12,  'ans':"The optimal change for an item that costs $0 with an amount paid of $89.12 is 1 $50 bill, 1 $20 bill, 1 $10 bill, 1 $5 bill, 4 $1 bills, 1 dime, and 2 pennies."}
]

tested_function = optimal_change
count = 0
total = len(tests)
for i in range(total):
    input1 = tests[i]['in1']
    input2 = tests[i]['in2']
    ans1 = tested_function(input1, input2)
    ans2 = tests[i]['ans']
    if(ans1 == ans2):
        print(f'Passed test {i+1} of {len(tests)}')
        count += 1
    else:
        print(f'Failed test {i+1} of {len(tests)}')

print(f'{count}/{total} tests passed.')