from datetime import date, timedelta


# date list
def date_range_list(days: int = 5):
    date_range = []

    current_date = date.today()
    end_date = date.today() + timedelta(days=days)

    while current_date < end_date:
        date_range.append(current_date.isoformat())
        current_date += timedelta(days=1)

    return date_range
