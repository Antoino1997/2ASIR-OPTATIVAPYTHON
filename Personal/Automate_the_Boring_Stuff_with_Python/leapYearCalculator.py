def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

while True:
    print('Enter a year or "done":')
    response = input()
    if response == 'done':
        break
    print('Is leap year:', is_leap_year(int(response)))