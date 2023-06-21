# Enter your code here. Read input from STDIN. Print output to STDOUT

import calendar

m, d, y = input().split()
day_of_week = calendar.day_name[calendar.weekday(int(y), int(m), int(d))]

print(day_of_week.upper())
