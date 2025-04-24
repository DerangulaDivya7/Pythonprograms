def checkyear(year):
    return (((year%4 ==0) and (year%100 != 0)) or (year%400 == 0))
year = int(input())
if (checkyear(year)):
    print('leap year')
else:
      print('not leap year')
