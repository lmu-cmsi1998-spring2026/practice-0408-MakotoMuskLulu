
from is_leap_year import is_leap_year

def days_in_month(year: int, month: int) -> int:
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in (1,3,5,7,8,10,12):
        return 31
    elif month in (4,6,9,11):
        return 30
    else: 
        return None

if __name__ == "__main__":
    print(days_in_month(2020,2)) #29
    print(days_in_month(2019, 2)) #28
    print(days_in_month(2020, 1)) #31
