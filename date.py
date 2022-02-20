# from datetime import datetime, timedelta, timezone
# dagens_datum = datetime.now()
# print('today is: ' + str(dagens_datum)) 
# one_day = timedelta(days=1978)
# igår = dagens_datum - one_day
# print('igår is: ' + str(igår)) 
# one_years = timedelta(days=365)
# igår = dagens_datum - one_years
# print('igår is: ' + str(igår))

# birthday = input('when is your birthday (dd/mm/yyyy)? ')
# birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
# print('Birthday: ', str(birthday_date)) 
print()
x = input('ange ett tal')
y = input('ange ett tal')

print()
try:
    print(int(x)/int(y))
except ZeroDivisionError as e:
    print('Aj aj aj ett fel')
else:
    print('Somthing else went wrong')
finally:
    print('this is our cleanup code')
print()