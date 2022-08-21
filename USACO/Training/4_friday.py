"""
ID: spencew2
LANG: PYTHON3
PROG: friday
"""

fin = open("friday.in", 'r')
fout = open("friday.out", 'w')

def isLeapYear(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      return False
    return True
  return False

year = 1900
MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
end_date = int(fin.readline()) + year
fridays = [0, 0, 0, 0, 0, 0, 1] # SUN, MON, TUES, WED, THURS, FRI, SAT
fridays_days = ["SUN", "MON", "TUES", "WED", "THURS", "FRI", "SAT"]
firstFriday = 6 #Saturday

while year < end_date:
  for x in range(0, 12):
    if x == 1 and isLeapYear(year):
      nextFriday = (firstFriday + ((MONTH_DAYS[x] + 1) % 7)) % 7
    else: nextFriday = (firstFriday + (MONTH_DAYS[x] % 7)) % 7
    if x!= 11 or year + 1 != end_date:
      print(fridays_days[nextFriday])
      fridays[nextFriday] = fridays[nextFriday] + 1
    firstFriday = nextFriday
  year += 1

fridays = [fridays[-1]] + fridays[:-1]
for x in range(0,7):
  fout.write(str(fridays[x]))
  if x == 6: fout.write('\n')
  else: fout.write(" ")

fout.close()