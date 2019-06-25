from datetime import timedelta, datetime


def get_first_day_week(signal):
    date_format = '%d' + signal + '%m' + signal + '%Y'

    current_day = datetime.today().date()
    next_day = current_day + timedelta(days=1)
    correct_format_next_day = next_day.strftime('%d/%m/%Y')

    datetime_format = datetime.strptime(correct_format_next_day, '%d/%m/%Y')

    monday_date = datetime_format - timedelta(days=datetime_format.weekday())
    monday_date = monday_date.strftime(date_format)

    return monday_date
