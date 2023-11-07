# welcome banner
heading =  '-' * 5 + ' FINANCIAL VISUALIZER ' + '-' * 5
line = '-' * len(heading)
print (line + '\n' + heading + '\n' + line)

# user input prompts
salary = input('Annual Salary:\n')
housing = input('Monthly Housing:\n')
bills = input('Monthly Bills:\n')
food = input('Weekly Food:\n')
travel = input('Annual Travel:\n')

# validating inputs
if salary.isnumeric() and housing.isnumeric() and bills.isnumeric() and food.isnumeric() and travel.isnumeric():
    print ('inputs confirmed valid')
else :
    print('invalid input, please try again')

# Taxes
if int(salary) >= 0 and int(salary) <= 10000 :
    tax = round(int(salary) * 5/100, 2)

elif int(salary) >= 10001 and int(salary) <= 40000 :
    tax = round(int(salary) * 10/100,2)

elif int(salary) >= 40001 and int(salary) <= 80000 :
    tax = round(int(salary) * 15/100, 2)

elif int(salary) >= 80001 :
    tax = round(int(salary) * 20/100, 2)

# Calculations

# Annual amounts
annual_housing = int(housing) * 12 
annual_bills = int(bills) * 12
annual_food = int(food) * 52
extra = int(salary) - tax - annual_bills - annual_food - annual_housing

# Percentages
perc_housing = round(annual_housing / int(salary) * 100, 2 )
perc_bills = round(annual_bills / int(salary) * 100, 2)
perc_food = round(annual_food / int(salary) * 100, 2)
perc_travel = round(int(travel) / int(salary) * 100, 2)
perc_tax = round(tax / int(salary) * 100 ,2)
perc_extra = round(extra / int(salary) * 100 ,2)

# Bars
housing_bar = '#' * int(perc_housing)
bills_bar = '#' * int(perc_bills)
food_bar = '#' * int(perc_food)
travel_bar = '#' * int(perc_travel)
tax_bar = '#' * int(perc_tax)
extra_bar = '#' * int(perc_extra)

# Table
width = int(max(perc_food, perc_bills, perc_extra, perc_housing, perc_tax, perc_travel))
boundary = '-' * width

print(boundary)
print(' housing ' + ' | ' + ' $ ' + str(annual_housing) + ' | ' + str(perc_housing) + ' | ' + housing_bar)
print('\n'+' bills ' + ' | ' + ' $ ' + str(annual_bills) + ' | ' + str(perc_bills) + ' | ' + bills_bar)
print('\n'+' food ' + ' | ' + ' $ ' + str(annual_food) + ' | ' + str(perc_food) + ' | ' + food_bar)
print('\n'+' travel ' + ' | ' + ' $ ' + str(travel) + ' | ' + str(perc_travel) + ' | ' + travel_bar)
print('\n'+' tax ' + ' | ' + ' $ ' + str(tax) + ' | ' + str(perc_tax) + ' | ' + tax_bar)
print('\n'+' extra ' + ' | ' + ' $ ' + str(extra) + ' | ' + str(perc_extra) + ' | ' + extra_bar)
print(boundary)