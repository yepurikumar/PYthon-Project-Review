type=input('enter the type:')
units=int(input('total units:'))
if type=='comertial':
    if units>=1 and units<=1000:
        total=units*12
        print(f'total amount is {total}')
    elif units>1000:
        total1=1000*12
        units=units-1000
        total=(units*15)+total1
        print(f'total amount is {total}')
    else:
        print(f'{units} are not valid')
elif type=='house':
    if units>=1 and units<=500:
        total=units*5
        print(f'total amount is {total}')
    elif units>500 and units<=1000:
        total1=500*5
        units=units-500
        total=(units*6)+total1
        print(f'total amount is {total}')
    elif units>1000 and units<20000:
        total1=500*5
        units=units-500
        if units>=1:
            total2=500*6
            units=units-500
            total=(units*7)+total1+total2
            print(f'total amount is {total}')
    else:
        print(f'{units} are not valid')
elif type=='factories':
    if units>=1 and units<=10000:
        total=units*15
        print(f'total amount {total}')
    elif units>10000 and units<=20000:
        total1=10000*15
        units=units-10000
        total=(units*18)+total1
        print(f'total amount is {total}')
    else:
        print(f'{units} are not valid')
else:
    print(f'{type} is invalid')
