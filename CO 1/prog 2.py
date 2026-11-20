import datetime

end = int(input("Enter final year: "))
start = datetime.date.today().year
for year in range(start, end + 1):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print(year, end=" ")