# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line
leek_price = 2
x=str(leek_price)
order = 'leek 4'
leek_number = int(order[5])
sum_total = leek_number * leek_price
broccoli = 2.34
order1 = 1.6
sum_totalbroccoli= broccoli *order1
sum_broccoli=round(sum_totalbroccoli,2)
print('Leek is ' + x + ' euro per kilo')
print(f'1.6 kg broccoli costs {sum_broccoli}e')