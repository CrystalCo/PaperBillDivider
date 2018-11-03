
def monopoly(dollar_amt, result=''):
    '''
    Accepts integer input that represents a dollar amount (dollar_amt) 
    and return a string indicating the most efficient set of paper bills
    to distribute evenly amongst players in Monopoly.
    '''

    # The set of paper bills available in the game
    values = [50, 20, 10, 5, 1]
    
    for list_value in values:
    
        if dollar_amt >= list_value:

            count = int(dollar_amt // list_value)

            result += '${} '.format(list_value) * count

            val = dollar_amt - (list_value * count)

            return monopoly(val, result)

    return result[:-1]

print(monopoly(88))
