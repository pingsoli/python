# 3.14 Finding the Date Range for the Current Month

from datetime import datetime, date, timedelta
import calendar

def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date, end_date)

first_day, last_day = get_month_range()
print(first_day, last_day)  # 2017-12-01 2018-01-01
