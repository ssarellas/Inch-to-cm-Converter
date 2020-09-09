#cm to inch conversion

print('Do you want to convert to cm or to inches? (input cm or inch)')
question = input()

if question == 'cm':
    print('how many inches?')
    inches = input()
    cm = float(inches) * 2.54
    print(inches,' inches is equal to ',round(cm,2), ' cm.''')
    
elif question == 'inch':
    print('how many centimetres?')
    cm = input()
    inch = float(cm) * 0.393
    print(cm,'centimetres is equal to ', round(inch,2),' inches.')

else:
    print('Please restart the program and enter either inch or cm')



