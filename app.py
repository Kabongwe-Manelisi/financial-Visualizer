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

#Taxes
if int(salary) >= 0 and int(salary) <= 10000 :
    tax = round(int(salary) * 5/100, 2)
    print(tax)

elif int(salary) >= 10001 and int(salary) <= 40000 :
    tax = round(int(salary) * 0.1,)
    print(tax)

elif int(salary) >= 40001 and int(salary) <= 80000 :
    tax = round(int(salary) * 15/100, 2)
    print(tax)

elif int(salary) >= 80001 :
    tax = round(int(salary) * 20/100, 2)
    print(tax)

