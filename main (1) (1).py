def isLeapYear(year):
  if(year % 4 == 0 and year % 100 !=0) or year  % 400 == 0:
    return True
  else:
    return False
    
year=int(input("enter a number:"))

if isLeapYear(year):
  print('{} is a Leap year.'.format(year))
else:
  print('{} is a Leap year.'.format(year))
  
