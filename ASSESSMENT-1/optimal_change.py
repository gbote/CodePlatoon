# Game Plan
# First compute the total change required back
   #-if customer didnt pay enough (negative value), notify of this
# Compute the optimal change combination to return the total
   #-for each currency denomination, starting at largest and moving smaller:
       #compute the number of times the current value divides evenly into the denomination (using //)
       #if greater than 1, record that number of times for that denomination and subtract from total change amount
# once optimal change by denomination computed, output the change in correct format
    #cycle through dictionary, getting count and using singular if =1 or plural if >1

denom = [
    {'value': 100, 'single': '$100 bill', 'plural': '$100 bills'}, 
    {'value': 50,  'single': '$50 bill',  'plural': '$50 bills'}, 
    {'value': 20,  'single': '$20 bill',  'plural': '$20 bills'}, 
    {'value': 10,  'single': '$10 bill',  'plural': '$10 bills'}, 
    {'value': 5,   'single': '$5 bill',   'plural': '$5 bills'}, 
    {'value': 1,   'single': '$1 bill',   'plural': '$1 bills'}, 
    {'value': .25, 'single': 'quarter',   'plural': 'quarters'}, 
    {'value': .1,  'single': 'dime',      'plural': 'dimes'}, 
    {'value': .05, 'single': 'nickel',    'plural': 'nickels'}, 
    {'value': .01, 'single': 'penny',     'plural': 'pennies'}
    ]

def optimal_change(cost, paid):  # sourcery skip: avoid-builtin-shadow
    
    # compute the change back to customer
    change = round(paid - cost, 2)

    # handle if customer paid exact amounts or not enough
    if change == 0:
        return 'No change required!'
    elif change < 0:
        return f"Sorry, you didn't pay enough. You must pay ${abs(change)} to buy this item"

    change_str = f'The optimal change for an item that costs ${cost} with an amount paid of ${paid} is'
    iter = 0
    # compute optimal denomination amounts for the change required
    for item in denom:
        divisible = change // item['value'] if change > .04 else change / item['value'] #handles the float-point issue with pennies
        
        if divisible >= 1:
            change = round(change -(divisible * item['value']), 2) #handle the float-point issue
            dollar_num = int(divisible)
            punctuation = ','
            if change == 0:
                punctuation = '.'
                if iter > 0: change_str += ' and'
            change_str += f" {dollar_num} {item['single'] if dollar_num==1 else item['plural']}{punctuation}"
            iter += 1
    return change_str
