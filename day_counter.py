
import sys
from is_valid_date import is_valid_date
from days_in_month import days_in_month


def day_counter(year1: int, month1: int, day1: int,
                year2: int, month2: int, day2: int) -> int:
    if not is_valid_date(year1, month1, day1):
        raise ValueError("First date is invalid")
    if not is_valid_date(year2, month2, day2):
        raise ValueError("Second date is invalid")


    if (year1, month1, day1) == (year2, month2, day2):
        return 0

   
    if (year1, month1, day1) > (year2, month2, day2):
        year1, month1, day1, year2, month2, day2 = year2, month2, day2, year1, month1, day1

    count = 0

    while (year1, month1, day1) != (year2, month2, day2):
        day1 += 1
        count += 1

        if day1 > days_in_month(year1, month1):
            day1 = 1
            month1 += 1

            if month1 > 12:
                month1 = 1
                year1 += 1

    return count


if __name__ == "__main__":
    if len(sys.argv) != 7:
        print("Usage: python3 day_counter.py <year1> <month1> <day1> <year2> <month2> <day2>")
        sys.exit(1)

    year1 = int(sys.argv[1])
    month1 = int(sys.argv[2])
    day1 = int(sys.argv[3])
    year2 = int(sys.argv[4])
    month2 = int(sys.argv[5])
    day2 = int(sys.argv[6])

    print(day_counter(year1, month1, day1, year2, month2, day2))


    if __name__ == "__main__":
        print(day_counter(2024, 2, 28, 2024, 3, 1))
=======
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
>>>>>>> b73f21faebb0f6ba1dfb98fdde728ca4f3612cae
