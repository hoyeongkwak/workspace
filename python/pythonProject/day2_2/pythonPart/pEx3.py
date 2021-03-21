score = int(input('input score:'))

if score > 90:
    print('{} grade A'.format(score))
elif score > 80:
    print('{} grade B'.format(score))
else:
    print('{} grade C'.format(score))
