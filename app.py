#welcome banner
heading =  '-' * 5 + ' FINANCIAL VISUALIZER ' + '-' * 5
line = '-' * len(heading)
print (line + '\n' + heading + '\n' + line)

#user input prompts
salary = input('Annual Salary:\n')
housing = input('Monthly Housing:\n')
bills = input('Monthly Bills:\n')
food = input('Weekly Food:\n')
travel = input('Annual Travel:\n')

#validating inputs
if salary.isnumeric() and housing.isnumeric() and bills.isnumeric() and food.isnumeric() and travel.isnumeric():
    print ('inputs confirmed valid')
else :
    print('invalid input, please try again')