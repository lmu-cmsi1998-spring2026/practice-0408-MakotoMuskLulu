from days_in_month import days_in_month


def is_valid_date(year, month, day):
    if month < 1 or month > 12:
        return False
    if day < 1 or day > days_in_month(year, month):
        return False
    return True


if __name__ == "__main__":
    print(is_valid_date(2020, 2, 29))  # True
    print(is_valid_date(2019, 2, 29))  # False
    print(is_valid_date(2020, 1, 31))  # True
    print(is_valid_date(2020, 4, 31))  # False
    print(is_valid_date(1938, 8, 31)) # True
    print(is_valid_date(1602, 9, 30)) # True
    print(is_valid_date(1602, 9, 31)) # False
