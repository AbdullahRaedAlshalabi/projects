'''
This is a program that you enter a certain number of days
and convert it to weeks, months and years
'''
print('——————————————————'.center(50))
print('hello, world!'.center(50))
print('——————————————————'.center(50))

try:
    number_of_days = int(input('Enter the number of days: '))
    
    # Convert to weeks
    weeks = number_of_days // 7
    days_remaining_after_weeks = number_of_days % 7
    
    # Convert to months (assuming 30 days per month)
    months = number_of_days // 30
    days_remaining_after_months = number_of_days % 30
    
    # Conversion to years (using 360 days per year)
    years = number_of_days // 360
    days_remaining_after_years = number_of_days % 360
    
    # Show Results
    print('–' * 50)
    print(f'{number_of_days} Day = {weeks} Week and {days_remaining_after_weeks} Day')
    print(f'{number_of_days} Day = {months} Month and {days_remaining_after_months} Day')
    print(f'{number_of_days} Day = {years} Year and {days_remaining_after_years} Day')
    print('–' * 50)

except ValueError:
    print("Error: Please enter a valid number!")
