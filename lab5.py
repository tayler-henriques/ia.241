#3.1
alien_color= 'yellow'
if alien_color =='green':
 print('You just earned 5 points')
 
#3.2
alien_color= 'green'
if alien_color =='green':
    print('you just earned 5 points')
else:
     print('player just earned 10 points')

#3.3
favorite_fruits=['strawberries', 'grapes', 'blackberries']
if 'strawberries' in favorite_fruits:
    print('You really like strawberries!')
if 'grapes' in favorite_fruits:
    print('You really like grapes!')
if 'blackberries' in favorite_fruits:
    print('You really like blackberries!')

#3.4
age= 17
if age < 10:
 print('you are a kid')
elif age < 20:
    print('you are a teenager')
else:
     print('you are an adult')
     if age > 65:
         print('you are an elder')