country =input('Were do you come from? ') 
if country.lower() == 'sweden':
    print('Du är från Sweden!') 
else:
    print('You are not from Sweden!!')


price =input('How much? ')
if float(price) >= 1.00:
    tax = .07
    print(tax)
else:
    tax = 0

price_tax = float(price) * (1 + tax)
print('please pay: ', price_tax) 
