day= int(input("enter day:"))
month = int(input("enter month:"))
year = int(input("enter year:"))
def converter(day, month, year):
    if month > 10 or day > 10 and month == 10:
        birthYear = year + 622
    else:
        birthYear = year + 621

    print(f"The year of your birthday is {birthYear}")


converter(day, month, year)