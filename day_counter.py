from sys import argv

from is_valid_date import is_valid_date


def day_counter(year1: int, month1: int, day1: int, year2: int, month2: int, day2: int) -> int:
    current_year = year1
    current_month = month1
    current_day = day1

    day_count = 0

    while (current_year, current_month, current_day) != (year2, month2, day2):
        day_count += 1
        current_day += 1

        if not is_valid_date(current_year, current_month, current_day):
            current_day = 1
            current_month += 1

            if not is_valid_date(current_year, current_month, current_day):
                current_month = 1
                current_year += 1

    return day_count


if len(argv) != 7:
    print("Usage: day_counter.py year1 month1 day1 year2 month2 day2")
else:
    try:
        year1, month1, day1, year2, month2, day2 = map(int, argv[1:])
        if (year1, month1, day1) > (year2, month2, day2):
            total_days = day_counter(year2, month2, day2, year1, month1, day1)
            print(f"There are {total_days} days between those dates.")
        else:
            total_days = day_counter(year1, month1, day1, year2, month2, day2)
            print(f"There are {total_days} days between those dates.")

    except ValueError:
        print("Please enter valid dates using whole numbers in YYYY MM DD format.")
